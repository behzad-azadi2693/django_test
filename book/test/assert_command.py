'''
assertEqual(a, b) ---> a == b

assertNotEqual(a, b) ---> a != b

assertTrue(x) ---> bool(x) is True

assertFalse(x) ---> bool(x) is False

assertIs(a, b) ---> a is b

assertIsNot(a, b) ---> a is not b

assertIsNone(x) ---> x is None

assertIsNotNone(x) ---> x is not None

assertIn(a, b) ---> a in b

assertNotIn(a, b) ---> a not in b

assertIsInstance(a, b) ---> isinstance(a, b)

assertNotIsInstance(a, b) ---> not isinstnace(a, b)

assertGreater(a, b) ---> a > b

assertGreaterEqual(a, b) ---> a >= b

assertLess(a, b) ---> a < b

assertLessEqual(a, b) ---> a <= b

assertRegexpMatches(s, r) ---> r.search(s)

assertNotRegexpMatches(a, b) ---> not r.search(s)

assertItemsEqual(a, b) ---> sorted(a) == sorted(b) ---> Works with unhashable objects

assertRaises(exc, fun, args, *kwds) ---> fun(*args, **kwds) raises exc

assertRaisesRegexp(exc, r, fun, args, *kwds) ---> round(a-b, 7) == 0

assertAlmostEqual(a, b) --> round(a-b, 7) == 0

assertNotAlmostEqual(a, b) ---> round(a-b, 7) != 0

assertFormError
assertTemplateUse(response, 'tmplate.addr)
'''