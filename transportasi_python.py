
import pulp

gudang = ['G1', 'G2', 'G3']
toko = ['T1', 'T2', 'T3', 'T4']

biaya = {
    ('G1','T1'):30000, ('G1','T2'):25000, ('G1','T3'):28000, ('G1','T4'):32000,
    ('G2','T1'):26000, ('G2','T2'):30000, ('G2','T3'):24000, ('G2','T4'):27000,
    ('G3','T1'):28000, ('G3','T2'):26000, ('G3','T3'):25000, ('G3','T4'):29000
}

kapasitas = {'G1':120, 'G2':180, 'G3':100}
permintaan = {'T1':150, 'T2':90, 'T3':80, 'T4':80}

model = pulp.LpProblem("Transportasi_PT_Ventico", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", (gudang, toko), lowBound=0)

model += pulp.lpSum(biaya[(i,j)] * x[i][j] for i in gudang for j in toko)

for i in gudang:
    model += pulp.lpSum(x[i][j] for j in toko) == kapasitas[i]

for j in toko:
    model += pulp.lpSum(x[i][j] for i in gudang) == permintaan[j]

model.solve()

for i in gudang:
    for j in toko:
        if x[i][j].value() > 0:
            print(f"{i} ke {j} = {x[i][j].value()}")

print("Total Biaya =", pulp.value(model.objective))
