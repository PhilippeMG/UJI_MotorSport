//---------------------Importar Librerias-----------------------
#include <WiFi.h>
#include <ESPAsyncWebServer.h>
#include <SPIFFS.h>


//---------------------Create AsyncWebServer object on port 80---------------------
AsyncWebServer server(80);

//---------------------Credenciales de WiFi-----------------------
const char* ssid = "MarcosWIFI";
const char* password = "marcos99";

//---------------------Variables Globales-------------------------
//------Potenciometer-----
const int potPin = 34;
int testValue = 0;
int iteration = 0;

//------WI-FI Conection-----
int contconexion = 0;

//---------------------Metodos-------------------------
String readSensor(){
  int value = analogRead(potPin);
  testValue = value;
  return String(value);
}

//---------------------------SETUP--------------------------------
void setup() {
  Serial.begin(115200);

  //-----------RED-----------
  //Conectando a la red WI-FI
  WiFi.begin(ssid, password);
  //Cuenta hasta 50 si no se puede conectar lo cancela
  while (WiFi.status() != WL_CONNECTED and contconexion <50) { 
    ++contconexion;
    delay(500);
    Serial.print(".");
  }
  //Ip asignada
  Serial.println();
  Serial.println(WiFi.localIP());

  // Initialize SPIFFS
  if(!SPIFFS.begin()){
    Serial.println("An Error has occurred while mounting SPIFFS");
    return;
  } else {
    Serial.println("SPIFFS loaded correctly");
  }
  
  //-----------SERVER | WEB-PAGE-----------


  //  File file = SPIFFS.open("/inx.html", FILE_READ);
  //  if(!file){
  //    Serial.println("FIle not found");
  //  }else{
  //    Serial.println("File loaded");
  //  }

  // Route for root / web page
  server.on("/", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send(SPIFFS, "/index.html");
  });

  server.on("/potencia", HTTP_GET, [](AsyncWebServerRequest *request){
    request->send_P(200, "text/plain", readSensor().c_str());
  });
 

  
  server.begin();

}

//----------------------------LOOP----------------------------------
void loop() {
}
