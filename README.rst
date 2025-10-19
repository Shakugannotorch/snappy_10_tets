The 10 tetrahedra cusped census database
============================

This repository stores the manifold database of a complete census of
all orientable cusped hyperbolic 3-manifolds triangulizable by no more than 10 tetrahedra, 
and includes the source code for the Python module
:code:`snappy_10_tets` which packages them up for use in SnapPy and
Spherogram.

To install the module in SageMath::

  sage -pip install git+https://github.com/Shakugannotorch/snappy_10_tets/

To use this module with SnapPy, one can do::

  sage: from snappy_10_tets import snappy

The extended census can then be accessed via SnapPy's :code:`Manifold` class. 
For example::

  sage: m = snappy.Manifold('o10_140311(1, 0)')
  sage: m.triangulation_isosig()
  'kLLPLPAkcdefhihgijjhsutktfkekj_baBb(1,0)'

For the 10-tetrahedra census, this module also stores all minimal triangulations of a given manifold,
which can be accessed by, for example::

  sage: m = snappy.Manifold('o10_140311')
  sage: m.isometry_class
  ['kLLLMzQkcdeghfhijjjhslmfnfumrf_bBba',
 'kLLLLQAkcdfhhigihjjhstrcrwkrps_abBa',
 'kLLPLPAkcdefhihgijjhsutktfkekj_baBb']

For census below 10-tetrahedra, :code:`m.isometry_class` has been extracted from `the Regina database <https://regina-normal.github.io/data.html>`_ , 
but is not perfectly compatible with SnapPy as of current, in the sense that one needs to create the manifold with :code:`snappy.TenTetCuspedCensus` instead of :code:`snappy.Manifold`, 
otherwise an error will be raised when one tries to access :code:`m.isometry_class`. 
Therefore the appropriate way to access it is::
  
  sage: m = snappy.TenTetCuspedCensus['o9_08594']
  sage: m.isometry_class
  ['jLALLAQcbbfgfhiiihhkltxkqdm',
 'jLALzMQbcbefgihhixxjnlotrsk',
 'jLAwwQPbcbdfghgiihhjqgxarxr']

Furthermore, the peripheral information in the census below 10-tetrahedra was not stored.

The raw source for the tables are in::
  
  manifold_src/original_manifold_sources

stored as plain text CSV files for the potential convenience of other
users. The triangulations themselves are stored in the "isosig" format
of Burton, as described in the appendix to `this paper
<http://arxiv.org/abs/1110.6080>`_ with an added "decoration" suffix
that describes the peripheral framing.
