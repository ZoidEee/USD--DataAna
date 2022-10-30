import pandas as pd
import plotly.graph_objs as go

maticData = pd.read_excel('Matic.xlsx')
optimismData = pd.read_excel('Optimism.xlsx')
binanceData = pd.read_excel('Binance.xlsx')


def estimate(amount):
    mAmount, bAmount, oAmount = amount, amount, amount

    mPay = [s.split('$')[1] for s in maticData['Amount']]
    oPay = [s.split('$')[1] for s in optimismData['Amount']]
    bPay = [s.split('$')[1] for s in binanceData['Amount']]
    for line in mPay:
        mAmount = mAmount * float(line) + mAmount

    for line in oPay:
        oAmount = oAmount * float(line) + oAmount

    for line in bPay:
        bAmount = bAmount * float(line) + bAmount

    return print(f'Matic (USD+): ${mAmount}\nOptimism (USD+): ${oAmount}\nBinance (USD+): ${bAmount}')


def apyPlot(average):
    mDates = list(maticData['Date'])
    mAPYdata = [line[:-1] for line in list(maticData['APY'])]
    mPay = [s.split('$')[1] for s in maticData['Amount']]
    data = []

    if average:
        avg = 0.0
        total = 0
        for line in mAPYdata:
            avg = avg + float(line)
            total += 1
        print(total)

        avg = avg / total
        a = 0

        while a != total:
            a += 1
            data.append(avg)

        '''fig = go.Figure([go.Scatter(x=mDates, y=mAPYdata)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()'''

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Matic USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()

    else:
        fig = go.Figure([go.Scatter(x=mDates, y=mAPYdata)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()


apyPlot(True)
