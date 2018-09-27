Getting started with the nodela API
########################################

.. toctree::
  :maxdepth: 3

Introduction
=============
Nodela has a Restful API with URL endpoints corresponding to actions that users can perform with their channels. The endpoints accept and return JSON encoded objects. The API URL path always contains the API version in order to differentiate queries to different API versions. All queries start with: ``/api/<version>/`` where ``<version>`` is an integer representing the current API version.

.. _chain-related-information:

ELA Mainchain API
=================================
using the following api ,we can easyly get a glimps of what is going on in the blockchain.

create a ELA wallet
-----------------------------------------
generate a elastos wallet 

.. http:get:: /api/1/createWallet

   **Example request**:

   .. sourcecode:: http

      GET /api/1/createWallet HTTP/1.1
      Host: localhost

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
          "result":{
              "privateKey":"492F67D441F563AA4746497EB77C89906A3D3C06B242030BA966BC5604482EF7",
              "publicKey":"035EBC0D70C9E34006C932D7BB47474159C136A8944C92416A94481212379751CB",
              "address":"EJonBz8U1gYnANjSafRF9EAJW9KTwRKd6x"
          },
          "status":200
      }

   :statuscode 200:   no error
   :statuscode 400:   bad request
   :statuscode 404:   not found request
   :statuscode 500:   internal error
   :statuscode 10001: process error
   


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

Signing message using private key   
-----------------------------------------

.. http:post:: /api/1/sign

   **Example request**:

   .. sourcecode:: http

    POST /api/1/sign HTTP/1.1
    Host: localhost:8090
    Content-Type: application/json

      {
          "privateKey":"0D5D7566CA36BC05CFF8E3287C43977DCBB492990EA1822643656D85B3CB0226",
          "msg":"你好，世界"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
          "result": {
              "msg": "E4BDA0E5A5BDEFBC8CE4B896E7958C",
              "pub": "02C3F59F337814C6715BBE684EC525B9A3CFCE55D9DEEC53E1EDDB0B352DBB4A54",
              "sig": "E6BB279CBD4727B41F2AA8B18E99B3F99DECBB8737D284FFDD408B356C912EE21AD478BCC0ABD65246938F17DDE64258FD8A9684C0649B23AE1318F7B9CEEEC7"
          },
          "status": 200
      }


verify message signed by a public address's private key  
--------------------------------------------------------

.. http:post:: /api/1/verify

   **Example request**:

   .. sourcecode:: http

    POST /api/1/verify HTTP/1.1
    Host: localhost
    Content-Type: application/json

      {
          "msg": "E4BDA0E5A5BDEFBC8CE4B896E7958D",
          "pub": "02C3F59F337814C6715BBE684EC525B9A3CFCE55D9DEEC53E1EDDB0B352DBB4A54",
          "sig": "E6BB279CBD4727B41F2AA8B18E99B3F99DECBB8737D284FFDD408B356C912EE21AD478BCC0ABD65246938F17DDE64258FD8A9684C0649B23AE1318F7B9CEEEC7"
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Vary: Accept
      Content-Type: application/json

      {
          "result": true,
          "status": 200
      }

create offline transaction
-----------------------------------------
create a offline transaction utxo json data , you should sign it using private key 

.. http:post:: /api/1/createTx

   **Example request**:

   .. sourcecode:: http

    POST /api/1/currHeight HTTP/1.1
    Host: localhost

      {
          "inputs"  : ["EU3e23CtozdSvrtPzk9A1FeC9iGD896DdV"],
           "outputs" : [{
                  "addr":"EPzxJrHefvE7TCWmEGQ4rcFgxGeGBZFSHw",
                   "amt" :1000
               }]
      }

   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
        "result": {
            "Transactions": [
                {
                    "UTXOInputs": [
                        {
                            "address": "EU3e23CtozdSvrtPzk9A1FeC9iGD896DdV",
                            "txid": "fa9bcb8b2f3a3a1e627284ad8425faf70fa64146b88a3aceac538af8bfeffd91",
                            "index": 1
                        }
                    ],
                    "Fee": 100,
                    "Outputs": [
                        {
                            "amount": 1000,
                            "address": "EPzxJrHefvE7TCWmEGQ4rcFgxGeGBZFSHw"
                        },
                        {
                            "amount": 99997800,
                            "address": "EU3e23CtozdSvrtPzk9A1FeC9iGD896DdV"
                        }
                    ]
                }
            ]
        },
        "status": 200
    }


send offline transaction
-----------------------------------------
send raw transaction 

.. http:post:: /api/1/sendRawTx

   **Example request**:

   .. sourcecode:: http

    POST /api/1/sendRawTx HTTP/1.1
    Host: localhost

      {
         "data":"0200010013313637333832373132343538363832353937350191FDEFBFF88A53ACCE3A8AB84641A60FF7FA2584AD8472621E3A3A2F8BCB9BFA01000000000002B037DB964A231458D2D6FFD5EA18944C4F90E63D547C5D3B9874DF66A4EAD0A3E80300000000000000000000214B177C93439E1E31B1CDA7C3B290F977C74CD0BFB037DB964A231458D2D6FFD5EA18944C4F90E63D547C5D3B9874DF66A4EAD0A368D8F5050000000000000000217779F85469B90D2F648D6BA771FB641D1782715E000000000141407009A5DAB9A8730ED424EF50217180D25AB81F0BB6E8257A672F9618F3CF13FD32D114DE171460C23532319A85614C460E83699C833E576B5C4782232299A2DF232103293CD3A3359B65FEA091CB6260675BD03A3C5E29CFFB504136A508E9BBBD5A8BAC"
      }
    
   **Example response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
          "result": "1f4432635bcf8c347f2bc20b7906c8c6c195f51beb3426e5f8d6a9e4cc073cf3",
          "status": 200
      }


.. _did-related-api:

ELA DID Sidechain API
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
    

