"""Figure 4: Economic cost, marginal cost and break-even from stated formulae."""
import numpy as np
import matplotlib;matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import total_cost,REVENUE,F,CF,CM
m=np.linspace(.5,70,2000)
fig,axs=plt.subplots(1,3,figsize=(18,5.6));a,b,c=axs
a.plot(m,total_cost(m),lw=2,label='Continuous cost');a.plot(m,total_cost(m,True),lw=1.1,alpha=.75,label='Discrete cost (ceil)');a.axhline(REVENUE,color='#139777',ls='--',label='Revenue 195,000 THB');a.axvline(12.27,ls=':',color='#e5a52a');a.set(xlim=(70,.5),ylim=(0,225000),xlabel='Motility (%) → Decreasing',ylabel='Breeding Cost (THB)',title='A. Cost vs Sperm Motility');a.legend(fontsize=8)
b.plot(m,(CM*(F/10)*70)/(m*m),color='#de7619',lw=2);b.axvline(12.27,ls=':',color='#e5a52a');b.set(xlim=(70,2.2),ylim=(0,4000),xlabel='Motility (%) → Decreasing',ylabel='Marginal Cost (THB per 1%-point)',title='B. Marginal Cost |dTC/dM|')
profit=REVENUE-total_cost(m);crit=(CM*(F/10)*70)/(REVENUE-F*CF)
c.plot(m,profit,color='#058c79',lw=2);c.fill_between(m,0,profit,where=profit>0,color='#059b87',alpha=.14);c.axhline(0,color='black',lw=.8);c.axvline(crit,ls=':',color='#dc991b',label=f'Continuous break-even {crit:.3f}%');c.set(xlim=(70,.5),xlabel='Motility (%) → Decreasing',ylabel='Net Profit (THB per cycle)',title='C. Break-even (Continuous Cost)');c.legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Economic model reconstruction: no empirically calibrated motility-to-hatching function',fontsize=12)
fig.tight_layout();fig.savefig('Figure4_economics.png',dpi=300);plt.close(fig)
