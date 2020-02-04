
import numpy as np

import matplotlib
import matplotlib.pyplot as plt

import seaborn as sns


def simulation_plot(data=None,x_axis=None,hline=None,ax=None,fig=None,x_lim=None,y_lim=None,y_axis_ticks=None,title='',x_label='',y_label='',fig_size=(20,6),
  scale='log',linewidth=0.7,hline_linewidth=2,alpha=0.1,hline_alpha=1):
  '''
  Produce a plot of a long run simulation

  Parameters
  ----------
  data : array_like (m,n), optional
    The simulation data to plot. Each row of the array represents one run of the simulation.
    These data are the y-axis values of the simulation
    This array does not contain the independent variable.
  x_axis : array_like (n,), optional
    The values of the independent variable, to plot the data of each run against.
    This data is the x-axis value of the simulation.
  hline : float
    The y-axis value at which to plot a horizontal line.
  ax : matplotlib.axes.Axis, optional
    The axis to plot on, if already configured.
  fig : matplotlib.figure.Figure, optional
    The figure to plot on, if already configured.
  x_lim : 2-tuple of floats, optional
    The left and right limit of the x-axis of the plot.
    These limits do not have to equal the smallest and largest value in x_axis.
  y_lim : 2-tuple of floats, optional
    The top and bottom limit of the y-axis of the plot.
  y_axis_ticks : array_like(k,)
    Locations of ticks along the y-axis.
  title : string, optional
    The title to appear on the plot.
  x_label : string, optional
   The label to appear on the x-axis of the plot.
  y_label : string, optional
   The label to appear on the y-axis of the plot.
  fig_size : string, optional
    The size to make the figure.
  scale : string, optional
    The scaling of the x-axis.
  linewidth : float, optional
    The linewith of each run's line.
  hline_linewidth : float, optional
    The linewith of the horizontal line.
  alpha : float, optional
    The alpha of each run's line.
  hline_alpha : float, optional
    The alpha of the horizontal line.

  Returns
  -------
  fig : matplotlib.figure.Figure
    The Figure with the simulation runs plotted
  ax : matplotlib.axes.Axis
    The Axis of the fig

  '''
  with _SimulationPlotStyle():
    # generate an axis if not passed in
    if ax is None:
      fig,ax=_setup_simulation_plot(x_lim=x_lim,y_lim=y_lim,y_axis_ticks=y_axis_ticks,title=title,x_label=x_label,y_label=y_label,
        fig_size=fig_size,scale=scale)
    # plot the data
    for datum in data:
      ax.plot(x_axis,datum,color="#1f77b4",linewidth=linewidth,alpha=alpha)
    # plot the horizontal line
    if hline is not None:
      ax.axhline(hline,color="#d62728",linewidth=hline_linewidth,alpha=hline_alpha)

  # if we have a figure as well as an axis
  if fig is not None:
    return fig,ax
  else:
    return ax

def setup_simulation_plot(x_lim=None,y_lim=None,y_axis_ticks=None,title='',x_label='',y_label='',fig_size=(20,6),scale='log'):
  '''
  Produce the base figure and axis for a simulation plot

  Parameters
  ----------
  x_lim : 2-tuple of floats, optional
    The left and right limit of the x-axis of the plot.
    These limits do not have to equal the smallest and largest value in x_axis.
  y_lim : 2-tuple of floats, optional
    The top and bottom limit of the y-axis of the plot.
  y_axis_ticks : array_like(k,)
    Locations of ticks along the y-axis.
  title : string, optional
    The title to appear on the plot.
  x_label : string, optional
   The label to appear on the x-axis of the plot.
  y_label : string, optional
   The label to appear on the y-axis of the plot.
  fig_size : string, optional
    The size to make the figure.
  scale : string, optional
    The scaling of the x-axis.

  Returns
  -------
  fig : matplotlib.figure.Figure
    A blank Figure
  ax : matplotlib.axes.Axis
    The Axis of the fig

  '''
  with _SimulationPlotStyle():
    fig,ax=_setup_simulation_plot(x_lim=x_lim,y_lim=y_lim,y_axis_ticks=y_axis_ticks,title=title,x_label=x_label,y_label=y_label,
      fig_size=fig_size,scale=scale)

  return fig,ax

class _SimulationPlotStyle(matplotlib.rc_context):
  '''
  Style a simulation plot without affecting the global plotting settings

  Plots are styled with the seaborn muted palette.
  '''
  def __init__(self, **kwargs):
    matplotlib.rc_context.__init__(self)
    sns.set_palette("muted",color_codes=True)
    sns.set()

def _setup_simulation_plot(x_lim=None,y_lim=None,y_axis_ticks=None,title='',x_label='',y_label='',fig_size=(20,6),scale='log'):
  '''
  Produce the base figure and axis for a simulation plot

  Parameters
  ----------
  x_lim : 2-tuple of floats, optional
    The left and right limit of the x-axis of the plot.
    These limits do not have to equal the smallest and largest value in x_axis.
  y_lim : 2-tuple of floats, optional
    The top and bottom limit of the y-axis of the plot.
  y_axis_ticks : array_like(k,)
    Locations of ticks along the y-axis.
  title : string, optional
    The title to appear on the plot.
  x_label : string, optional
   The label to appear on the x-axis of the plot.
  y_label : string, optional
   The label to appear on the y-axis of the plot.
  fig_size : string, optional
    The size to make the figure.
  scale : string, optional
    The scaling of the x-axis.

  Returns
  -------
  fig : matplotlib.figure.Figure
    A blank Figure
  ax : matplotlib.axes.Axis
    The Axis of the fig

  '''
  fig,ax=plt.subplots(figsize=fig_size)
  ax.set_xscale(scale)

  # turn off vertical grid lines, style horizontal grid lines
  ax.grid(False,'both','x')
  ax.grid(True,'major','y',color='k',linestyle='-',linewidth=0.8,alpha=0.3)
  
  # set the limits
  if x_lim is not None: ax.set_xlim(x_lim[0],x_lim[1])
  if y_lim is not None: ax.set_ylim(y_lim[0],y_lim[1])

  # set the ticks
  if y_axis_ticks is not None: ax.set_yticks(np.arange(*y_axis_ticks))

  # set the style of the borders
  for side in ['left','bottom','right','top']:
    ax.spines[side].set_linewidth(0.7)
    ax.spines[side].set_color('#333333')

  # style ticks
  ax.tick_params(axis="x",which="both",top=False,bottom=True,width=0.7,labelsize=14)
  ax.tick_params(axis="y",which="both",left=True,direction="inout",width=0.7,labelsize=14)
  ax.tick_params(axis="y",which="both",right=True,direction="in",width=0.7,labelsize=14)

  # set titles and labels
  ax.set_xlabel(x_label,fontsize=16)
  ax.set_ylabel(y_label,fontsize=16)
  ax.set_title(title,fontsize=18)

  return fig,ax
