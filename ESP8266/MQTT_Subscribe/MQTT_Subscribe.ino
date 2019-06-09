#include <ESP8266WiFi.h> 
#include <PubSubClient.h>

const char* ssid = "NETGEAR17";
const char* wifi_password = "huskybox224";

const char* mqtt_server = "192.168.1.6";
const char* mqtt_topic = "test";
const char* mqtt_username = "atharv";
const char* mqtt_password = "athu1996";

const char* clientID = "Bedroom Table";

WiFiClient wifiClient;
PubSubClient client(mqtt_server, 1883, wifiClient); // 1883 is the listener port for the Broker

void ReceivedMessage(char* topic, byte* payload, unsigned int length) 
{
  String a;
  for (int i=0; i<length; i++){
    a = a + (char)payload[i];
  }
  Serial.println(a);
}

bool Connect() 
{
  if (client.connect(clientID, mqtt_username, mqtt_password)) {
      client.subscribe(mqtt_topic);
      Serial.println("Connected");
      return true;
    }
    else {
      Serial.println("Trying again");
      return false;
  }
}

void setup() 
{
  Serial.begin(115200);

  Serial.print("Connecting to ");
  Serial.println(ssid);
  
  WiFi.begin(ssid, wifi_password);
  
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("WiFi connected");
  Serial.print("IP address: ");
  Serial.println(WiFi.localIP());

  client.setCallback(ReceivedMessage);
  if (Connect()) {
    Serial.println("Connected Successfully to MQTT Broker!");  
  }
  else {
    Serial.println("Connection Failed!");
  }
}

void loop() 
{
  if (!client.connected()) {
    Connect();
  }
  client.loop();
}
