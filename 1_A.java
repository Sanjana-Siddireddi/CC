HelloPublisher.java:

import javax.xml.ws.Endpoint;

public class HelloPublisher {
    public static void main(String[] args) {
        String url = "http://localhost:9090/hello";
        Endpoint.publish(url, new HelloService());
        System.out.println("SOAP Service running at: " + url + "?wsdl");
    }
}
__________________
HelloService.java:

import javax.jws.WebService;

@WebService(targetNamespace="http://soapdemo/")
public class HelloService {
    public String sayHello(String name) {
        return "Hello " + name + ", welcome to SOAP Web Service!";
    }
}
__________________
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" 
                  xmlns:ser="http://soapdemo/">
   <soapenv:Header/>
   <soapenv:Body>
      <ser:sayHello>
         <name>Name</name>
      </ser:sayHello>
   </soapenv:Body>
</soapenv:Envelope>
