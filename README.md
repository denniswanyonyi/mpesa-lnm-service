

## M-PESA Lipa Na Mpesa API Service

Service consumes M-PESA API exposed via Daraja

## Overview

M-Pesa works by sending two requests:-
    
(a) C2B Validation - which alllows the web service to respond with either success or failure in order to either complete or cancel a transaction. This option can be enabled or disabled and as such this request is optional.

(b) C2B Confirmation - which is an acknowledgment that a transaction was successful on M-PESA. This request is mandatory if Validation and Confirmation URLs are registered on M-PESA

The URL structure will be as below

Validation URL: http://IP:PORT/c2b/validation

Confirmation URL: http://IP:PORT/c2b/confirmation

The IP can be the load balanced IP that forwards traffic to the deployed application. The port will be what's provisioned on the load balancer. If using a direct server IP to the application, then the IP can be server IP and the port can be 8000, which is the default port in django.

### C2B Validation Request Payload


`{
   "TransactionType":"Pay Bill", 
   "TransID":"QD3J8AZH6T",
   "TransTime":"20220201064858",
   "TransAmount":"1500",
   "BusinessShortCode":"123123",
   "BillRefNumber":"202020",
   "InvoiceNumber":"",
   "OrgAccountBalance":"6549197.00",
   "ThirdPartyTransID":"",
   "MSISDN":"254720123123",
   "FirstName":"Dennis",
   "MiddleName":"",
   "LastName":"Wanyonyi"
}`


## Build Docker Image

The project comes with a Dockerfile that can be used to build this django project to a docker image. The name of the image is up to you but for the commands below, we'll name the image the same as the project. In order to build a docker image, ensure you have docker installed on your machine and run below command

`docker build -t lnm_service .`

