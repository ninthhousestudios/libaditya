# TODO

## Argala equal-count tiebreaker

`calc/jaimini.py`, `argala()` method (~line 186).

When argala and virodha graha counts are equal, the method unconditionally marks the argala as obstructed:

```python
if arg.how_many_grahas() == vir.how_many_grahas():
    obstructed.append(arg.grahas())
```

Per traditional Jaimini (and matching Arrow's implementation), equal counts should be broken by first-strength sign ranking — the same `fs.index()` comparison already used in the `arg < vir` branch:

```python
if arg.how_many_grahas() == vir.how_many_grahas():
    if fs.index(vir) > fs.index(arg):
        argala.append(arg.grahas())
    else:
        obstructed.append(arg.grahas())
```

Surfaced by fletch-astro sweep tests (fletch-astro/14). All other Jaimini calculations (karakas, padas, sign strengths, bandhana yogas) agree across engines.
