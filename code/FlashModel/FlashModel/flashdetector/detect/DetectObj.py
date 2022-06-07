import cv2,time,json
import tensorflow as tf
import numpy as np
from datetime import datetime
from PIL import Image
from .object_detection import ObjectDetection
from azure.iot.device import IoTHubDeviceClient, Message, IoTHubModuleClient

import os
ospath = os.path.dirname(os.path.abspath(__file__))
print(ospath)
MODEL_FILENAME = os.path.join(ospath,'model.pb')
LABELS_FILENAME = os.path.join(ospath,'labels.txt')

labels = None

#azure connection string
# CONNECTION_STRING = ""

def iothub_client_init():
    # Create an IoT Hub client
    # client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    client =IoTHubModuleClient.create_from_edge_environment()
    return client

def create_telemetry(telemetry_msg, component_name=None):
    """
    Function to create telemetry for a plug and play device. This function will take the raw telemetry message
    in the form of a dictionary from the user and then create a plug and play specific message.:param telemetry_msg: A dictionary of items to be sent as telemetry.
    :param component_name: The name of the device like "sensor"
    :return: The message.
    """
    msg = Message(json.dumps(telemetry_msg))
    msg.content_encoding = "utf-8"
    msg.content_type = "application/json"
    if component_name:
        msg.custom_properties["$.sub"] = component_name
    return msg
# MSG_TXT = '{{"pigcount": {count},"deviceid": '+str(CONNECTION_STRING.split(";")[1].split("=")[1])+'}}' 
# MSG_TXT = '{{"Object": {obj},"Confidence":{conf}}}' 

def log_msg(msg):
    print("{}: {}".format(datetime.now(), msg))

class TFObjectDetection(ObjectDetection):
    """Object Detection class for TensorFlow"""

    def __init__(self, graph_def, labels):
        super(TFObjectDetection, self).__init__(labels)
        self.graph = tf.compat.v1.Graph()
        with self.graph.as_default():
            input_data = tf.compat.v1.placeholder(tf.float32, [1, None, None, 3], name='Placeholder')
            tf.import_graph_def(graph_def, input_map={"Placeholder:0": input_data}, name="")

    def predict(self, preprocessed_image):
        inputs = np.array(preprocessed_image, dtype=np.float)[:, :, (2, 1, 0)]  # RGB -> BGR

        with tf.compat.v1.Session(graph=self.graph) as sess:
            output_tensor = sess.graph.get_tensor_by_name('model_outputs:0')
            outputs = sess.run(output_tensor, {'Placeholder:0': inputs[np.newaxis, ...]})
            return outputs[0]
            
def initialize():
    print('Loading model...', end='')
    graph_def = tf.compat.v1.GraphDef()
    with open(MODEL_FILENAME, 'rb') as f:
        graph_def.ParseFromString(f.read())
    print('Success!')

    print('Loading labels...', end='')
    with open(LABELS_FILENAME, 'r') as f:
        labels = [l.strip() for l in f.readlines()]
    print("{} found. Success!".format(len(labels)))
    
    global od_model
    od_model = TFObjectDetection(graph_def, labels)
    return od_model
     
def predict_image(self,image):
    log_msg('Predicting image')

    w, h = image.size
    log_msg("Image size: {}x{}".format(w, h))

    predictions = self.od_model.predict_image(image)

    response = {
        'id': '',
        'project': '',
        'iteration': '',
        'created': datetime.utcnow().isoformat(),
        'predictions': predictions }
        
    log_msg('Results: ' + str(response))
    return response

class DetectCount:
    def __init__(self):
        self.client = iothub_client_init()
        self.client.connect()
        self.od_model = initialize()
        time.sleep(0.1)

    def __del__(self):
        self.video.release()

    def get_frame(self,frame,min_conf_threshold):
        height,width,_ = frame.shape
        screen = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        response = predict_image(self,Image.fromarray(screen))
        print(min_conf_threshold)
        for i in response["predictions"]:
            if i["probability"] > min_conf_threshold:
                x = int(i["boundingBox"]["left"]*width)
                y = int(i["boundingBox"]["top"]*height)
                w = int(i["boundingBox"]["width"]*width)
                h = int(i["boundingBox"]["height"]*height)
                print(x,y,w,h)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,128), 5)
                # msg_txt_formatted = MSG_TXT.format(obj=i["tagName"],conf=i["probability"])
                # message = Message(msg_txt_formatted)
                temperature_msg1 = {"data":{"Object": str(i["tagName"]),"confidence":i["probability"]}}
                msg = create_telemetry(temperature_msg1)
                print( "Sending message: {}".format(msg) )
                self.client.send_message(msg)
                print ( "Message successfully sent" )
        #time.sleep(5)
        #cv2.putText(frame,str(count), (10,80), cv2.FONT_HERSHEY_SIMPLEX, 3, 255)
        return frame