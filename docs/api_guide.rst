Getting started with the nodela API
########################################

.. toctree::
  :maxdepth: 3

Introduction
=============
Nodela has a Restful API with URL endpoints corresponding to actions that users can perform with their channels. The endpoints accept and return JSON encoded objects. The API URL path always contains the API version in order to differentiate queries to different API versions. All queries start with: ``/api/<version>/`` where ``<version>`` is an integer representing the current API version.

.. _chain-related-information:

Chain Related Api
=================================
using the following api ,we can easyly get a glimps of what is going on in the blockchain.


Check the current network block height
-----------------------------------------
tells you the current block height of the network 

.. http:get:: /api/1/currHeight

   **Example request**:

   .. sourcecode:: http

    GET /api/1/currHeight HTTP/1.1
    Host: localhost

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "result": 128797,
        "status": 200
      }

   :statuscode 200:   no error
   :statuscode 400:   bad request
   :statuscode 404:   not found request
   :statuscode 500:   internal error
   :statuscode 10001: process error
   
Get the transactions of specific height   
-----------------------------------------
using height to get block contained transactions 

.. http:get:: /api/1/txs/(int:`block_height`)

   get the transactions that the user (`block_height`) wrote.

   **Example request**:

   .. sourcecode:: http

    GET /api/1/txs/10 HTTP/1.1
    Host: localhost

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
        "result": {
            "Transactions": [
                "53b06e08da9362abf50003e26f8b99b38bd32b6a7dfad83203ef5bb9da2f4a05"
            ],
            "Height": 10,
            "Hash": "1166ae059fd6914a44edde9aa8a2765138da0ab868ddaeb51d20d21908c488da"
        },
        "status": 200
      }


.. _did-related-api:

DID Related Api 
====================
using the following api , get the did related information

Create DID
---------------
create a did with the correspond private key.

.. http:get:: /api/1/did
   
   **Example Request**:

   .. sourcecode:: http

      GET /api/1/did HTTP/1.1
      Host: localhost

   **Example Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "result": {
            "privateKey": "6E228664BE94833BB18DF6C66BE09173A8F42856E27CCF3DDEADE5785C16FDF7",
            "did": "iXMBmDBXtqTEyiKEVga9dUNqhJBvE74Ln9"
        },
        "status": 200
      }
    

Retrive DID
---------------
using private key to retrive did .

.. http:get:: /api/1/did/(string:`private_key`)
   
   **Example Request**:

   .. sourcecode:: http

      GET /api/1/did/6E228664BE94833BB18DF6C66BE09173A8F42856E27CCF3DDEADE5785C16FDF7 HTTP/1.1
      Host: localhost

   **Example Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "result": "iXMBmDBXtqTEyiKEVga9dUNqhJBvE74Ln9",
        "status": 200
      }
    

