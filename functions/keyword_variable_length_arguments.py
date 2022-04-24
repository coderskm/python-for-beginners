def printDict(**paraDict):
  for d,v in paraDict.items():
    print(f"key={d} its value={v}")

printDict(id="007", item="gadget watch", brand="omega", name="james bond")
printDict(id="009", item="gadget airplane", brand="stealth", name="jack ryan")
