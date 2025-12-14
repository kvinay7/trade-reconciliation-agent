from lib.csv_reader import read_csv_any

sample = b"TradeRef,Qty,Px\nT1,10,100\nT2,20,200"
df = read_csv_any(sample)

assert list(df.columns) == ["TradeRef", "Qty", "Px"]
assert len(df) == 2

print("CSV ingestion test passed")
