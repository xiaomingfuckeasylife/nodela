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

.. http:example:: curl wget httpie python-requests

    GET /api/1/currHeight HTTP/1.1
    Host: localhost

Get the transactions of specific height   
-----------------------------------------
using height to get block contained transactions 

.. http:example:: curl wget httpie python-requests

    GET /api/1/txs/10 HTTP/1.1
    Host: localhost


.. _did-related-api:

DID Related Api 
====================
using the following api , get the did related information

Create DID
---------------
create a did with the correspond private key.

.. http:get:: /api/1/did
   
   **Example Request**:

   .. http:example:: curl wget httpie python-requests

      GET /api/1/address HTTP/1.1
      Host: localhost:5001

   **Example Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
          "our_address": "0x2a65Aca4D5fC5B5C859090a6c34d164135398226"
      }
    **Example Response**:

   .. sourcecode:: http

      HTTP/1.1 200 OK
      Content-Type: application/json

      {
          "our_address": "0x2a65Aca4D5fC5B5C859090a6c34d164135398226"
      }

Retrive DID
---------------
using private key to retrive did .

.. http:example:: curl wget httpie python-requests

    GET /api/1/did/446F426F20974A04D0A29974AE2C209DF11B55961288A718CD2D74F6D6FC2DC1 HTTP/1.1
    Host: localhost


