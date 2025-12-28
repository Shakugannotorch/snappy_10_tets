The database for 10-tetrahedra census of orientable cusped hyperbolic 3-manifolds
============================

This repository stores the manifold database of a complete census of
all orientable cusped hyperbolic 3-manifolds whose minimal ideal triangulations consist of no more than 10 tetrahedra,
accompanying the paper 

  Shana Yunsheng Li, The complete 10-tetrahedra census of orientable cusped hyperbolic 3-manifolds `arXiv:2512.02142
  <https://arxiv.org/abs/2512.02142>`_

and includes the source code for the Python module
:code:`snappy_10_tets` which packages them up for use in SnapPy.

To install the module in SageMath::

  sage -pip install git+https://github.com/Shakugannotorch/snappy_10_tets/

To use this module with SnapPy, one can do::

  sage: from snappy_10_tets import snappy

The extended census can then be accessed via SnapPy's :code:`Manifold` class. 
For example::

  sage: m = snappy.Manifold('o10_140311(1, 0)')
  sage: m.triangulation_isosig()
  'kLLLLQMkccefgihhjjjlnxcvsnwdau_baBb(1,0)'

For the 10-tetrahedra census, this module also stores all minimal triangulations of a given manifold,
which can be accessed by, for example::

  sage: m = snappy.Manifold('o10_140311')
  sage: m.isometry_class
  ['kLLLALQkccfgehhijjjlnhqadatjno',
 'kLLLLQPkbcghgfhijjjtsmssoswqhq',
 'kLLLwMQkcdefhhjhijjhftasjewesk',
 'kLLLMwQkbdgfhfjijijdwxxgrdphdw',
 'kLLLwMQkbcgffihijjjtsmqfakqdus',
 'kLLLLQMkccefgihhjjjlnxcvsnwdau',
 'kLLLzQMkcdehfgihjjjhftxwnhkujw',
 'kLLvAQPkcdfgghiijjjtcaljseaiew',
 'kLvLAAQkcfheigihjjjllhhksfnqlh',
 'kLvLMPQkbehggijgijjxptxgcqgnxp',
 'kLvLLQQkbeghgihjjijxpxvgvnjokj',
 'kvLLAAQkcffghiihjjjvhuumpcscsb',
 'kvLLAMQkdfgehhijijjnlxnxgjnngn',
 'kvLLAAQkcgfhhfjijijkqeatqbgroc']

For census below 10-tetrahedra, :code:`m.isometry_class` has been extracted from the `Regina database <https://regina-normal.github.io/data.html>`_ , 
but is not perfectly compatible with SnapPy as of current, in the sense that one needs to create the manifold with :code:`snappy.TenTetCuspedCensus` instead of :code:`snappy.Manifold`, 
otherwise an error will be raised when one tries to access :code:`m.isometry_class`. 
Therefore the appropriate way to access it is::

  sage: m = snappy.TenTetCuspedCensus['o9_08594']
  sage: m.isometry_class
  ['jLALLAQcbbfgfhiiihhkltxkqdm',
 'jLALzMQbcbefgihhixxjnlotrsk',
 'jLAwwQPbcbdfghgiihhjqgxarxr']

Furthermore, the peripheral information in the census below 10-tetrahedra was not stored.

The iterator for all manifolds in this module is :code:`snappy.TenTetCuspedCensus`. For example::
  
  sage: for M in snappy.TenTetCuspedCensus[-9:-6]: print(M, M.volume()) 
  o10_150721(0,0)(0,0)(0,0) 10.1494160640965
  o10_150722(0,0)(0,0)(0,0) 10.1494160640965
  o10_150723(0,0)(0,0) 10.1494160640965

  sage: for M in snappy.TenTetCuspedCensus(num_cusps=2)[-3:]: print(M, M.volume(), M.num_cusps())
  o10_150719(0,0)(0,0) 10.1494160640965 2
  o10_150723(0,0)(0,0) 10.1494160640965 2
  o10_150726(0,0)(0,0) 10.1494160640965 2

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other
users. The triangulations themselves are stored in the "isosig" format
of Burton, as described in the appendix to `this paper
<http://arxiv.org/abs/1110.6080>`_ with an added "decoration" suffix
that describes the peripheral framing.
