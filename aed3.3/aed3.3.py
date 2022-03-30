import matplotlib.pyplot as plt

y1 = [1.0028150081634521, 1.2699458599090576, 1.5191898345947266, 1.2725059986114502, 1.4248909950256348, 1.7930080890655518, 2.360146999359131, 2.8485679626464844, 3.2169840335845947, 3.335799217224121]
y2 = [0.797868013381958, 1.4457769393920898, 1.9262018203735352, 1.2731389999389648, 1.4508321285247803, 1.683121919631958, 2.030048131942749, 2.405480146408081, 2.73862886428833, 3.3601789474487305]
y3 = [0.7466089725494385, 1.3629848957061768, 1.594796895980835, 1.477963924407959, 1.6790049076080322, 2.094960927963257, 2.4941799640655518, 2.863687038421631, 3.3324520587921143, 3.6862871646881104]
y4 = [0.7485949993133545, 2.034105062484741, 1.99996018409729, 2.1019999980926514, 2.6289727687835693, 2.855001926422119, 2.7720019817352295, 3.072998046875, 4.542001962661743, 4.302998065948486]
y5 = [0.8419699668884277, 2.0164899826049805, 1.9861822128295898, 1.4531102180480957, 1.7780101299285889, 1.991765022277832, 2.4540350437164307, 2.709995985031128, 3.0580148696899414, 4.145012855529785]
y6 = 0.7709989547729492, 1.5626440048217773, 2.0323948860168457, 2.187363862991333, 2.1534039974212646, 2.0149989128112793, 2.410999059677124, 2.7039999961853027, 3.2770040035247803, 3.847994804382324
y7 = [0.8720991611480713, 1.710028886795044, 1.456969976425171, 1.3750338554382324, 1.379997968673706, 1.6809558868408203, 2.093998908996582, 2.615964889526367, 3.033003807067871, 3.3529670238494873]

y8 = [0.6590011119842529, 1.184000015258789, 1.457000970840454, 0.9270310401916504, 0.8489971160888672, 1.0460290908813477, 1.127964973449707, 1.243001937866211, 1.5189659595489502, 1.626033067703247, 1.7329978942871094, 1.9199779033660889, 2.1319620609283447, 2.7199997901916504, 2.891016960144043, 3.2989661693573, 3.388005018234253, 3.8000049591064453, 3.9130139350891113]

y1 = [67.54331636428833, 79.38826537132263, 87.66018795967102, 110.48483061790466, 135.69821286201477, 155.33499550819397, 162.29616475105286, 181.97237515449524, 190.67032957077026, 217.56910395622253, 245.6258475780487]

Y = list()
to = [y1, y2, y3, y4, y5, y6, y7]
for i in range(len(y1)):
    max = 5
    for j in to:
        if j[i] < max:
            max = j[i]
    Y.append(max)

x = [i for i in range(500000, 1050000, 50000)]

print(x)
plt.plot(x, y)

plt.show()















