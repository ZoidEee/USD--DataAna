import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

maticData = pd.read_excel('Matic.xlsx')
optimismData = pd.read_excel('Optimism.xlsx')
binanceData = pd.read_excel('Binance.xlsx')


def estimate(amount, network):
    mAmount, bAmount, oAmount = amount, amount, amount
    option = ['M', 'O', 'B']

    mPay = [s.split('$')[1] for s in maticData['Amount']]
    oPay = [s.split('$')[1] for s in optimismData['Amount']]
    bPay = [s.split('$')[1] for s in binanceData['Amount']]
    mL = []

    if network == option[0]:
        for line in mPay:
            oAmount = oAmount * float(line) + oAmount
            mL.append(oAmount)
        return mL
    elif network == option[1]:
        for line in mPay:
            mAmount = mAmount * float(line) + mAmount
            mL.append(mAmount)
        return mL
    elif network == option[2]:
        for line in mPay:
            bAmount = bAmount * float(line) + bAmount
            mL.append(bAmount)
        return mL
    elif network != any(option):
        print(f'Error in network:{option}, Please try again ')
        return


    for line in oPay:
        oAmount = oAmount * float(line) + oAmount

    for line in bPay:
        bAmount = bAmount * float(line) + bAmount


def get_avg(apyL):
    total_added = 0.0
    ct = 0.0
    for line in apyL:
        total_added = total_added + float(line)
        ct += 1.0

    avg = total_added / ct

    apy_list = []
    count = 0.0
    while count != ct:
        count += 1
        apy_list.append(avg)

    return apy_list


def apyPlot(network):
    options = ['O','M','B']

    if network == options[0]:
        mDates = list(optimismData['Date'])
        mAPYdata = [line[:-1] for line in list(optimismData['APY'])]
        fig = go.Figure([go.Scatter(x=mDates, y=mAPYdata)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return
    elif network == options[1]:
        mDates = list(maticData['Date'])
        mAPYdata = [line[:-1] for line in list(maticData['APY'])]
        fig = go.Figure([go.Scatter(x=mDates, y=mAPYdata)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return
    elif network == options[2]:
        mDates = list(binanceData['Date'])
        mAPYdata = [line[:-1] for line in list(binanceData['APY'])]
        fig = go.Figure([go.Scatter(x=mDates, y=mAPYdata)])
        fig.update_layout(autotypenumbers='convert types')
        fig.show()
        return
    elif network != any(options):
        print(f'Error in network:{network}, Please try again!')

    mDates = list(maticData['Date'])
    mAPYdata = [line[:-1] for line in list(maticData['APY'])]
    fig = go.Figure([go.Scatter(x=mDates, y=mAPYdata)])
    fig.update_layout(autotypenumbers='convert types')
    fig.show()


def avgApyPlot(network):
    option = ['O','M','B']

    if network == option[0]:
        mDates = list(optimismData['Date'])
        mAPYdata = [line[:-1] for line in list(optimismData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Optimism USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return
    elif network == option[1]:
        mDates = list(maticData['Date'])
        mAPYdata = [line[:-1] for line in list(maticData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Matic USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return
    elif network == option[2]:
        mDates = list(binanceData['Date'])
        mAPYdata = [line[:-1] for line in list(binanceData['APY'])]

        data = get_avg(mAPYdata)

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')))
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Average APY", mode="lines",
                                 line=dict(shape='linear', color='#000000', width=2, dash='dash'), connectgaps=True))
        fig.update_layout(
            title="Binance USD+ Daily APY + AVG APY", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
        return
    elif network != any(option):
        print(f'Error in network:{network}, Please try again!')
        return

def avgProfitPlot(deposit, net):
    option = ['O', 'M', 'B']
    deposit = float(deposit)

    if net == option[0]:
        mDates = list(optimismData['Date'])
        mAPYdata = [line[:-1] for line in list(optimismData['APY'])]

        data = estimate(deposit, option[0])

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=['0', '1500'], scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif net == option[1]:
        mDates = list(maticData['Date'])
        mAPYdata = [line[:-1] for line in list(maticData['APY'])]

        data = estimate(deposit, option[1])

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=['0', '1500'], scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    elif net == option[2]:
        mDates = list(binanceData['Date'])
        mAPYdata = [line[:-1] for line in list(binanceData['APY'])]

        data = estimate(deposit, option[2])

        fig = make_subplots(specs=[[{"secondary_y": True}]])
        fig.add_trace(go.Scatter(x=mDates, y=mAPYdata, name="Daily APY", mode="lines", line=dict(color='#1c95e7')),
                      secondary_y=False)
        fig.add_trace(go.Scatter(x=mDates, y=data, name="Deposit", mode="lines"), secondary_y=True)
        fig.update_yaxes(showgrid=False, secondary_y=True, range=['0', '1500'], scaleanchor='y2',
                         title='Deposit Estimation')

        fig.update_layout(
            title="USD+ Estimation", xaxis_title="Date", yaxis_title="APY",
            autotypenumbers='convert types'
        )
        fig.show()
    else:
        print(f'Error in {net}: please try again')
        return


avgApyPlot('M')