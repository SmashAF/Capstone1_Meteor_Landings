


'''
Hypothesis Test 1


Data:
 Africa           2351
 Antarcitica     21325
 Australia         383
 Blacksite        1648
 China              41
 Europe             72
 India              18
 Japan              12
 Middle East      1579
 New Zealand         1
 SouthAmerica      405
 USA               684

Total: 28519
'''






































# # Meteoroids observed falling per region per decade
# Europe_part1 = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>37) & (meteorites.reclat<66) 
#                     & (meteorites.reclong>-25) & (meteorites.reclong<26)]
# Europe_part2 = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>42) & (meteorites.reclat<66) 
#                     & (meteorites.reclong>26) & (meteorites.reclong<50)]
# frames = [Europe_part1,Europe_part2] # 2 frames needed to go around Turkey
# Europe = pd.concat(frames)
# Europe = Europe['year']
# India = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>8) & (meteorites.reclat<30) 
#                     & (meteorites.reclong>70) & (meteorites.reclong<88)]['year']
# Japan = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>29) & (meteorites.reclat<41) 
#                     & (meteorites.reclong>128) & (meteorites.reclong<145)]['year']
# China = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>20) & (meteorites.reclat<120) 
#                     & (meteorites.reclong>100) & (meteorites.reclong<125)]['year']
# Africa = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>-36) & (meteorites.reclat<36) 
#                     & (meteorites.reclong>-17) & (meteorites.reclong<44)]['year']
# USA = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>25) & (meteorites.reclat<49) 
#                     & (meteorites.reclong>-125) & (meteorites.reclong<-67)]['year']
# SouthAmerica = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>-56) & (meteorites.reclat<12) 
#                     & (meteorites.reclong>-81) & (meteorites.reclong<-34)]['year']
# #
# regionlist=[Japan,India,Europe,USA,China,Africa,SouthAmerica]



# meteorclean[location] = 'Europe' if (meteorclean.reclat>37) and (meteorclean.reclat<66) and (meteorclean.reclong>-25) & (meteorclean.reclong,26)


# def location(x):
#     if (x['reclat'] >37) and (x['reclat'] <66) and (x['reclong'] >-25) and (x['reclong']< 26):
#         return 'Europe'
#     elif (x['reclat'] >42) and (x['reclat'] <66) and (x['reclong'] >26) and (x['reclong']< 50):
#         return 'Europe'
#     elif (x['reclat'] >8) and (x['reclat'] <30) and (x['reclong'] >70) and (x['reclong']< 88):
#         return 'India'
#     elif (x['reclat'] >29) and (x['reclat'] <41) and (x['reclong'] >128) and (x['reclong']<145):
#         return 'Japan'    
#     elif (x['reclat'] >20) and (x['reclat'] <120) and (x['reclong'] >100) and (x['reclong']<125):
#         return 'China'
#     elif (x['reclat'] >-36) and (x['reclat'] <36) and (x['reclong'] >-17) and (x['reclong']<44):
#         return 'Africa'            
#     elif (x['reclat'] >25) and (x['reclat'] <49) and (x['reclong'] >-125) and (x['reclong']<-67):
#         return 'USA'    
#     elif (x['reclat'] >-56) and (x['reclat'] <12) and (x['reclong'] >-81) and (x['reclong']<-34):
#         return 'SouthAmerica'        
#     else:
#         return 'blacksite'
    
    
    
    
    
    
# df2 = df2.assign(flag=df2.apply(color_selector, axis=1))



# SouthAmerica = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>-56) & (meteorites.reclat<12) 
#                     & (meteorites.reclong>-81) & (meteorites.reclong<-34)]['year']

# meteorclean['location'] =['Europe' if ['reclat'] ['reclat'] <66 and x['reclong'] >-25 and x['reclong']< 26):
    
    
#  Europe_part2 = meteorites[(meteorites.fall=='Fell') & (meteorites.reclat>42) & (meteorites.reclat<66) 
#                     & (meteorites.reclong>26) & (meteorites.reclong<50)]   
 
 
 
#  Fall vs Found?? 
 
 
 
 
#  # Sample classification
 
#  fig = plt.figure(figsize=(15,5))
# ax = fig.add_axes([0,0,1,1])
# ax.plot(sample_recclass.value_counts(),linewidth=4)
# ax.set_title('Classification of Meteorites')
# labels = ax.set_xticklabels(sample_recclass.value_counts().index,rotation=90)
# ax.set_xlabel('Classifiers')
# ax.set_ylabel('Counts')
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
#  # Load libraries
# library(ggplot2) # Data visualization
# library(data.table)
# library(GGally)
# library(dplyr)
# library(RColorBrewer)

 
 
 
 
#  39.066670, 58.866670
 
#  # Throw away all meteorites with masses too large
# cutoff = 200
# mass = valid[valid['mass']<cutoff]
# #ObsMass = fell[fell['mass']<cutoff]
# ObsMass = fell[fell['mass']<2e4]
# # Compute the median and quantile of masses
# median = valid['mass'].median()
# q1 = valid['mass'].quantile(0.25)
# q2 = valid['mass'].quantile(0.75)
# ObsMedian = fell['mass'].median()
# Obsq1 = fell['mass'].quantile(0.25)
# Obsq2 = fell['mass'].quantile(0.75)

# # Create Histogram for all meteorites
# mass.hist(column='mass', bins=cutoff, xlabelsize=12, ylabelsize=12, figsize=(9,6), \
#             label='mass in gram, binsize=1', color='k')
# plt.axvline(median, label='median={0:.1f}g'.format(median), color='g')
# plt.axvline(q1, label='25% quantile={0:.1f}g'.format(q1), color='r')
# plt.axvline(q2, label='75% quantile={0:.1f}g'.format(q2), color='b')
# plt.legend(loc=9, prop={'size':15})
# plt.title('mass histogram of all meteorites', fontsize=20)


# MeteoritesCount %>%
    
#     ggplot(aes(x = recclass,y = Count)) +
#     geom_bar(stat='identity',colour="white", fill = fillColor) +
#     geom_text(aes(x = recclass, y = 1, label = paste0("(",Count,")",sep="")),
#               hjust=0, vjust=.5, size = 4, colour = 'black',
#               fontface = 'bold') +
#     labs(x = 'Meteorites Class', 
#          y = 'Count', 
#          title = 'Meteorites Class and Count') +
#     coord_flip() + 
#     theme_bw()
    
    
    
    

# Make a List of large meteorite landing locations for each 20-year period between 1700 and 2020:
# In[]:=
# locationsByTimePeriod=Table[largeMeteorites[Select[!MissingQ[#Year]&&DateObject[{maxYear-20}]<#Year<DateObject[{maxYear}]&],"Coordinates"],{maxYear,1720,2020,20}];
# Create a Table of the GeoListPlots of large meteorite landing locations for each List in locationsByTimePeriod:
# In[]:=
# geoListPlots=Table[GeoListPlot[locationsByTimePeriod[[n]],PlotLabelToString[n*20+1680]<>"-"<>ToString[n*20+1700],GeoCenter{0,0},GeoRangeAll],{n,Length@locationsByTimePeriod}];
# Animate the locations of recorded large meteorite landings in each 20-year period between 1700 and 2020:
# In[]:=
# ListAnimate[geoListPlots,AnimationRate1]
