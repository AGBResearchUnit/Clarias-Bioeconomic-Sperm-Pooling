"""Figure 5: Five-year NPV reconstructed from paper model, with published traditional case."""
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import SCENARIOS,male_count,REVENUE,F,CF,CM,UNCOMPENSATED_PROFIT,annual_npv
cases=[]
for name,m,color in SCENARIOS:
    n=male_count(m);profit=REVENUE-F*CF-CM*n;cases.append((name,m,color,n,profit))
cases.append(('Uncompensated traditional',12.27,'#d94d16',10,UNCOMPENSATED_PROFIT))
fig,ax=plt.subplots(figsize=(12,7));years=list(range(6))
markers=['o','^','D','s','x']
for i,(name,m,color,n,profit) in enumerate(cases):
    values=[0]+[annual_npv(profit,y) for y in years[1:]]
    ax.plot(years,np.array(values)/1e6,marker=markers[i],lw=2.2,color=color,label=f'{name} ({m:g}% motility)')
    ax.annotate(f'{values[-1]:,.0f} THB',(5,values[-1]/1e6),xytext=(8,0),textcoords='offset points',fontsize=9,color=color,va='center')
ax.set(xlim=(0,6.2),xlabel='Year (3 production cycles/year)',ylabel='Cumulative NPV (million THB)',title='5-Year Cumulative NPV Comparison (8% annual discount rate)')
ax.set_xticks(years);ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=9)
fig.tight_layout();fig.savefig('Figure5_NPV.png',dpi=300);plt.close(fig)
for name,m,color,n,profit in cases: print(name,'males=',n,'profit/cycle=',profit,'NPV=',round(annual_npv(profit,5)))
