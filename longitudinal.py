"""Figure 3: Differential cost & illustrative exponential decline (r unverified)."""
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
r=.25 # illustrative ONLY, not fitted to longitudinal data
M0=70.;m=np.linspace(4.7,70,900);t=np.linspace(0,10,500); mt=M0*np.exp(-r*t)
fig,axs=plt.subplots(1,3,figsize=(17,5.3))
a,b,c=axs
a.plot(m,70/m**2,color='#ea6a12',lw=2)
a.axvline(12.27,ls=':',color='grey');a.fill_between(m,0,70/m**2,where=m<15,color='#ea6a12',alpha=.12)
a.set(xlim=(70,4.7),xlabel='Sperm Motility (%) → Decreasing',ylabel='Magnitude |dy/dM|',title='A. Marginal Male Requirement')
b.plot(t,mt,lw=2,color='#0870a7');b.axhline(12.27,ls='--',color='#e2a12c',label='Observed 12.27%');b.fill_between(t,mt,alpha=.12)
b.set(xlabel='Time (years; illustrative)',ylabel='Sperm Motility (%)',title=f'B.1 Illustrative Motility Decay (r={r}/year)');b.legend(fontsize=8)
c.plot(t,70/mt,color='#c85592',lw=2);c.fill_between(t,70/mt,alpha=.10,color='#c85592');c.set(xlabel='Time (years; illustrative)',ylabel='Required Males per 10 Females',title='B.2 Illustrative Male Requirement Growth')
for ax in axs: ax.grid(alpha=.2)
fig.suptitle('Illustrative degradation model; rate r has not been independently validated',fontsize=12)
fig.tight_layout();fig.savefig('Figure3_longitudinal.png',dpi=300);plt.close(fig)
