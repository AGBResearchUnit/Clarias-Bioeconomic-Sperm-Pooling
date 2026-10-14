"""Figure 2: Continuous sperm motility vs male requirement per ten females."""
import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from model import males_per_ten
m=np.linspace(4.5,85,1200)
fig,ax=plt.subplots(figsize=(12,7))
ax.plot(m,males_per_ten(m),lw=2.7,color='#0870a7',label='Required males: continuous curve')
ax.axhline(1,ls='--',lw=2,color='#129673',label='Traditional ratio (1 male : 10 females)')
ax.axvline(70,ls=':',lw=1.5,color='#129673')
markers=[('Random Mix',6.135,(-1.1,1.1)),('CGA_A (White Testis)',12.27,(1.3,.9)),('Elite CGA_A',29,(1.2,.9)),('Normal Baseline',70,(1.1,.45))]
for name,x,offset in markers:
    y=float(males_per_ten(x));ax.scatter([x],[y],s=90,color='#c96810',edgecolor='black',linewidth=.5,zorder=4)
    ax.annotate(f'{name}\n({x:.1f}%, {y:.1f} males)',(x,y),xytext=(x+offset[0],y+offset[1]),fontsize=10,bbox=dict(boxstyle='round',fc='white',ec='#cccccc',alpha=.95))
ax.set(xlim=(0,85),ylim=(0,15),xlabel='Sperm Motility (%)',ylabel='Required Males (per 10 Females)',title='Impact of Sperm Motility on Breeding Ratio (per 10 Females)')
ax.grid(alpha=.2);ax.legend(loc='upper right');fig.tight_layout();fig.savefig('Figure2_compensation.png',dpi=300);plt.close(fig)
