//https://www.youtube.com/watch?v=rlecwJulJw0&list=PL2xmtLUbEugnUoLiRTqwCm5wi2MSzsw3D&index=7&t=0s
#include <WiFi.h>

//------------------Servidor Web en puerto 80---------------------


WiFiServer server(80);
//---------------------Credenciales de WiFi-----------------------

const char* ssid     = "Mi_Wifi";
const char* password = "qwerty1234";




//---------------------VARIABLES GLOBALES-------------------------
int contconexion = 0;

String header; // Variable para guardar el HTTP request

String estadoSalida = "off";

const int salida = 2;
//Pines del sensor y variable de almacenar datos
const int potPin = 4;
int potValue = 0;

//------------------------CODIGO HTML------------------------------
String pagina = 
"<script>"

"function exportTableToExcel(tableID, filename = ''){     var downloadLink;     var dataType = 'application/vnd.ms-excel';     var tableSelect = document.getElementById(tableID);"
    "var tableHTML = tableSelect.outerHTML.replace(/ /g, '%20');"  
   " filename = filename?filename+'.xls':'excel_data.xls';"
    
    "downloadLink = document.createElement('a');"
    
    "document.body.appendChild(downloadLink);"
    
    "if(navigator.msSaveOrOpenBlob){"
       " var blob = new Blob(['ufeff', tableHTML], {            type: dataType        });"
       " navigator.msSaveOrOpenBlob( blob, filename);"
   " }else{   "    
      "  downloadLink.href = 'data:' + dataType + ', ' + tableHTML;"
    
       " downloadLink.download = filename;"
        
       " downloadLink.click();"
   " }"
"}"
"</script> <!DOCTYPE html> <html xmlns:th='http://www.thymeleaf.org'>"
"<head>     <title>UJI MotorSport</title>     <meta charset='UTF-8' />"
    "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css' />      <style type='text/css'>         H1 { text-align: center}"
       "#BLANC { color: #FFFFFF; } </style>"
"</head> <body> <div class='container'> <h1 > Lectura de Sensors - UJI MotorSport -</h1>"

"<table class='table table-striped' id='tblData'>"

    " <tr>         <th>Sensor</th>         <th>Informació</th>         <th>Data</th>     </tr>";
String pagina2 = "</table>"


"<a  id='BLANC' class='btn btn-success' role='button' onclick=\"exportTableToExcel('tblData','dades_UMS')\">Exportar</a>"
"<a  id='BLANC' class='btn btn-warning' role='button' onclick='history.go(0)'>Refrescar</a>" 
"<a href='/on' class='btn btn-success' role='button'>ON</a>"
"<a href='/off' class='btn btn-danger' role='button' >OFF</a>"

"</div> </body> </html>";

  String datos="";
   
  int variable=0;
//---------------------------SETUP--------------------------------
void setup() {
  #include <time.h>
  Serial.begin(115200);
  Serial.println("");
  
  pinMode(salida, OUTPUT); 
  digitalWrite(salida, LOW);

  // Conexión WIFI
  WiFi.begin(ssid, password);
  //Cuenta hasta 50 si no se puede conectar lo cancela
  while (WiFi.status() != WL_CONNECTED and contconexion <50) { 
    ++contconexion;
    delay(500);
    Serial.print(".");
  }
  if (contconexion <50) {
      //para usar con ip fija
      IPAddress ip(192,168,43,60); 
      IPAddress gateway(192,168,43,1); 
      IPAddress subnet(255,255,255,0); 
      WiFi.config(ip, gateway, subnet); 
      
      Serial.println("");
      Serial.println("WiFi conectado");
      Serial.println(WiFi.localIP());
      server.begin(); // iniciamos el servidor
  }
  else { 
      Serial.println("");
      Serial.println("Error de conexion");
  }
}

//----------------------------LOOP----------------------------------

void loop(){
  WiFiClient client = server.available();   // Escucha a los clientes entrantes

  if (client) {                             // Si se conecta un nuevo cliente
    Serial.println("New Client.");          // 
    String currentLine = "";                //
    while (client.connected()) {            // loop mientras el cliente está conectado
      if (client.available()) {             // si hay bytes para leer desde el cliente
        char c = client.read();             // lee un byte
        Serial.write(c);                    // imprime ese byte en el monitor serial
        header += c;
        if (c == '\n') {                    // si el byte es un caracter de salto de linea
          // si la nueva linea está en blanco significa que es el fin del 
          // HTTP request del cliente, entonces respondemos:
          if (currentLine.length() == 0) {
            client.println("HTTP/1.1 200 OK");
            client.println("Content-type:text/html");
            client.println("Connection: close");
            client.println();
            
            // enciende y apaga el GPIO
            if ( header.indexOf("GET /on") >= 0) {
              Serial.println("GPIO on");
              estadoSalida = "on";
              digitalWrite(salida, HIGH);
            } else if (header.indexOf("GET /off") >= 0) {
              Serial.println("GPIO off");
              estadoSalida = "off";
              digitalWrite(salida, LOW);
            }
              potValue = analogRead(potPin);
              Serial.println(potValue);

            // Muestra la página web
            time_t t = time(NULL);
            struct tm tm = *localtime(&t);

            
            String date = (tm.tm_year + 1900) + "/" +(tm.tm_mon + 1) +'/' + (tm.tm_mday) + ':'+ tm.tm_hour + ':' + tm.tm_min + ':' + tm.tm_sec;
            datos= datos+"  <tr>         <td>Temp Motor</td>        <td>"+ potValue+"</td>        <td>"+ date+"</td>    </tr>";
            client.println(pagina+datos+pagina2);
            
            // la respuesta HTTP temina con una linea en blanco
            client.println();
                      //              delay(5000);

            break;
          } else { // si tenemos una nueva linea limpiamos currentLine
            currentLine = "";
          }
        } else if (c != '\r') {  // si C es distinto al caracter de retorno de carro
          currentLine += c;      // lo agrega al final de currentLine
        }
      }
    }
    // Limpiamos la variable header
    header = "";
    // Cerramos la conexión
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }
}
