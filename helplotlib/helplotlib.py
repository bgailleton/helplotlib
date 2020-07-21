"""Main module and only file?."""
from matplotlib import pyplot as plt
import matplotlib as mpl


def mkfig_simple_bold(fontsize_major = 12, fontsize_minor = 10, family = "arial" , **kwargs):

	mpl.rcParams["font.weight"] = "bold"
	mpl.rcParams["font.size"] = fontsize_major
	mpl.rcParams["font.family"] = family
	mpl.rcParams["axes.labelweight"] = "bold"
	mpl.rcParams["axes.labelsize"] = fontsize_minor

	fig,ax = plt.subplots(**kwargs)

	return fig,ax

def mkfig_grey_bold(fontsize_major = 12, fontsize_minor = 10, family = "arial" , **kwargs):

	mpl.rcParams["font.weight"] = "bold"
	mpl.rcParams["font.size"] = fontsize_major
	mpl.rcParams["font.family"] = family
	mpl.rcParams["axes.labelweight"] = "bold"
	mpl.rcParams["axes.labelsize"] = fontsize_minor

	fig,ax = plt.subplots(**kwargs)
	ax.set_facecolor('#cccccc')
	ax.grid(ls = '--', color = "w", alpha = 0.5)

	return fig,ax


def make_axis_log(fig, ax, x=True, y=True):
	"""
		
	"""
 	if(x):
	 	ax.set_xscale('log')
 	if(y):
	 	ax.set_yscale('log')