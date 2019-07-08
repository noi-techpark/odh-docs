
Glossary
========

.. glossary::
   :sorted:

   API
      The Application Programming Interface is a collection of methods
      that a software program makes available to allow interaction
      with other programs 
      
   Domain
      A domain is a category of interest to which one or more datasets
      belong to.

   Dataset
      A dataset is a collection of records from a Data source. See the
      :ref:`detailed description <dataset-def>`.

   Data format
      Data format is the way information is encoded and exchanged between
      applications.

   JSON
      The JavaScript Object Notation is a lightweight data format to
      ease the exchange of data between computer and its understanding
      for humans. Essentially a JSON file is a sequence of key-value
      pairs, organised into lists (arrays, sequences,
      vectors). Nesting of key-values and of lists is supported.

   Key-value
      Also called name-value pair or attribute-name pair, a key-value
      pair is a simple data structure in which information are stored
      as tuples {attribute, value}, with no constraint of uniqueness
      on both attribute and value.
     
   Data Source
      A Data Source is the origin of a dataset. See the
      :ref:`detailed description <data-source-def>`.


   Data Collector   
      A component of the |odh|\, a data collector is used to gather
      data from datasets and send them to the |odh|\. See the
      :ref:`detailed description <data-collector-def>`.
	    
   DTO   
      A core component of the |odh|\, the DTO transforms the data
      format of a Source into a |odh|\-understandable format.  See the
      :ref:`detailed description <dto-def>`.
   
   Writer   
      The Writer is a core component of the |odh|\. It receives data
      from the Data Collectors and stores them in the Database.  See
      the :ref:`detailed description <writer-def>`.

   DAL      
      The |dal| is used by the reader and writer to communicate with
      the database.  See the :ref:`detailed description <dal-def>`.
   
   Database      
      Also known as persistence layer, the database ("DB") stores all
      the data received by the writer. See the :ref:`detailed
      description <database-def>`.

   Reader      
      A core component of the |odh|\, the Reader extract data form the
      Database and sends it to the web services.  See the
      :ref:`detailed description <reader-def>`.

   Web Services
      In the context of the |odh| Project, web services expose to Data
      Consumers the data received from the reader. See the
      :ref:`detailed description <ws-def>`.

   Data Consumers      
      Applications that use data received from the Web Services.  See
      the :ref:`detailed description <data-consumer-def>`.


   Persistence layer      
      Another name for Database, see the above entry or the
      :ref:`detailed description <database-def>`.

   Claim
     In JSON Web Token, a claim is a piece of information about a
     subject, structured as a key/value pair.


   JSON Web Token
     It is a mechanism to exchange a claim between two parties, used
     for authentication purposes when the claim is digitally signed
     and/or encrypted.

   Statistical graphics   
     Statistical graphics are means to display statistical data with
     the purpose to ease their interpretations. Common statistical
     graphics include pie charts, histograms, and scatter plot.

   ODHtags
     In the tourism domain, this name refers to all the tags/filter
     that refer to data that have been validated by the Open Data Hub
     team.
