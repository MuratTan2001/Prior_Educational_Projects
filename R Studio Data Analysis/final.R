#201805072_201805051_201805044
DatasetNA<-read.csv("./DatasetNA.txt", sep="", stringsAsFactors=TRUE)

#===============================!!!!----Please run these functions once.----!!!!============================

#taking specified groups and returning their ID
ObservationNum<-function(specified1="No",specified2="No",Var1=1,Var2=2,dataframe=DatasetNA){
  myList<-list()
  if(specified1=="No"&& specified2=="No"){
    i<-1
    while(i<=100){
      if((is.na(DatasetNA[[3+Var1]][i])||is.na(DatasetNA[[3+Var2]][i]))){
        i=i+1
        next
      }
      myList<-append(myList,i)
      i=i+1
    }
    return(myList)
  }
  if(specified1!="No"&& specified2!="No"){
    i<-1
    while(i<=100){
      if(is.na(DatasetNA[[3+Var1]][i])||is.na(DatasetNA[[3+Var2]][i])){
        i=i+1
        next
      }
      if(specified1==as.character(DatasetNA$Gender[i])&&specified2==as.character(DatasetNA$Group[i])){
        myList<-append(myList, i)
      }
      i=i+1
    }
    return(myList)
  }
  if(specified1 !="No"|| specified2!="No"){
    if(specified1 !="No"){hi<-specified1}
    if(specified2 !="No"){hi<-specified2}
    i<-1
    while(i<=100){
      if(is.na(DatasetNA[[3+Var1]][i])||is.na(DatasetNA[[3+Var2]][i])){
        i=i+1
        next
      }
      if(hi==as.character(DatasetNA$Gender[i])||hi==as.character(DatasetNA$Group[i])){
        myList<-append(myList, i)
      }
      i=i+1
    }
  }
  return(myList) 
}
#Sorting the Observations to a Data frame
Listing<-function(specified1="No",specified2="No",Var1=1,Var2=2) {
  List<-ObservationNum(specified1=specified1,specified2=specified2,Var1=Var1,Var2=Var2)
  Numlist<-list()
  X<-unlist(List)
  for(i in 1:length(List)){
    Num<-DatasetNA[[Var1+3]][X[i]]
    Numlist<-append(Numlist,Num)
  }
  Numlist2<-list()
  for(i in 1:length(List)){
    Num<-DatasetNA[[Var2+3]][X[i]]
    Numlist2<-append(Numlist2,Num)
  }
  NumList<-data.frame(Numlist,Numlist2)
  return(NumList)
}
Dataframe<-Listing(specified1 = "Female",specified2 = "Group1",Var1 = 1,Var2 = 2)
#Calculate 2.Version
Calculate<-function(var1=1,var2=1,Specified1 = "No",Specified2 = "No"){
  list<-ObservationNum(specified1 = Specified1,specified2 = Specified2,Var1 = var1,Var2 = var2)
  c<-length(list)
  b<-c()
  for(i in 1:c){
    d<-list[[i]]
    unstable <- DatasetNA[[var1+3]][d]
    unstable <- gsub(",",".",unstable)
    unstable <- as.numeric(unstable)
    b<-append(b,unstable)
  }
  b<-sort(b)
  
  Min<-b[1]
  Max<-b[c]
  Median<-0
  
  if(c %% 2==0){
    Median<-b[c/2]+b[c/2+1]
  }
  else{
    Median<-b[(c+1)/2]
  }
  
  Range<-Max-Min
  Sum<-0
  for(i in 1:c){
    Sum<-b[i]+Sum
  }
  
  Mean<-Sum/c
  
  SumofSquare<-0
  for(i in 1:c){
    SumofSquare<-(b[i]-Mean)^2+SumofSquare
  }
  
  Variance<-0
  Variance_Var2<-0
  for(i in 1:c){
    Variance_Var1<-b[i]-Mean
    Variance_Var2<-Variance_Var1*Variance_Var1+Variance_Var2
  }
  Variance<-sqrt(Variance_Var2/c)
  
  Standard_deviation<-0
  Deviation_Var2<-0
  for(i in 1:c){
    Deviation_Var1<-b[i]-Mean
    Deviation_Var2<-Deviation_Var1*Deviation_Var1+Deviation_Var2
  }
  Standard_deviation<-sqrt(Deviation_Var2/(c-1))
  
  Frame<-data.frame(Min,Max,Range,Sum,Mean,Median,SumofSquare,Variance,Standard_deviation)
  return(Frame)
}
#Calculate 2 variables 2.Version
Calculate_Second<-function(Var_1=1,Var_2=2,Spec1="No",Spec2="No"){
  Frame_Var1<-Calculate(var1=Var_1,var2=Var_2,Specified1 = Spec1,Specified2 =Spec2)
  Frame_Var2<-Calculate(var1=Var_2,var2=Var_1,Specified1 = Spec1,Specified2 =Spec2)
  List<-ObservationNum(specified1 = Spec1,specified2 = Spec2,Var1 = Var_1,Var2 = Var_2)
  num       <- length(List)
  Mean_Var1 <- Frame_Var1$Mean[1]
  Mean_Var2 <- Frame_Var2$Mean[1]
  Stand_Var1 <- Frame_Var1$Standard_deviation[1]
  Stand_Var2 <- Frame_Var2$Standard_deviation[1]
  Cross_productVar1 <- Frame_Var1$SumofSquare[1]
  Cross_productVar2 <- Frame_Var2$SumofSquare[1]
  
  Cross_product<-0
  for (i in 1:num){
    Var_X <- as.numeric(gsub(",",".",DatasetNA[[Var_1+3]][List[[i]]]))
    Var_Y <- as.numeric(gsub(",",".",DatasetNA[[Var_2+3]][List[[i]]]))
    Cross_productVar1<-(Var_X-Mean_Var1)
    Cross_productVar2<-(Var_Y-Mean_Var2)
    Cross_product<- Cross_productVar1*Cross_productVar2+Cross_product
  }
  Covariance<-0
  for(i in 1:num){
    Var_X <- as.numeric(gsub(",",".",DatasetNA[[Var_1+3]][List[[i]]]))-Mean_Var1
    Var_Y <- as.numeric(gsub(",",".",DatasetNA[[Var_2+3]][List[[i]]]))-Mean_Var2
    Covariance<-Var_X*Var_Y/(num-1)+Covariance
  }
  Correlations<-0
  Correlations_Var1<-Stand_Var1*Stand_Var2
  Correlations<-Covariance/Correlations_Var1
  Frame<-data.frame(Cross_product,Covariance,Correlations)
  return(Frame)
}
Dataframing<-function(specified1="No",specified2="No",Var1=1,Var2=2) {
  List<-ObservationNum(specified1=specified1,specified2=specified2,Var1=Var1,Var2=Var2)
  Numlist<-c()
  X<-unlist(List)
  for(i in 1:length(List)){
    Num<-DatasetNA[[Var1+3]][X[i]]
    Num<-(sub(",", ".", as.character(Num)))
    Numlist<-append(Numlist,Num)
  }
  Numlist2<-c()
  for(i in 1:length(List)){
    Num<-DatasetNA[[Var2+3]][X[i]]
    Num<-(sub(",", ".", as.character(Num)))
    Numlist2<-append(Numlist2,Num)
  }
  tn<-data.frame(Numlist,Numlist2)
  
  return(tn)
}
Data_Frame<-Dataframing()
#Drawers
DrawIt<-function(specified1="No",specified2="No",Var1=1,Var2=2,Title="Scatter Plot of Xp and Yk Variables",Xlab="Xp variable",Ylab="Yk variable"){
  List<-ObservationNum(specified1=specified1,specified2=specified2,Var1=Var1,Var2=Var2)
  Data_Frame<-Dataframing(specified1=specified1,specified2=specified2,Var1=Var1,Var2=Var2)
  Xp<-c()
  for(i in 1:length(List)){
    Num<-Data_Frame[[1]][i]
    Num<-(as.numeric(Num))
    Xp<-append(Xp,Num)
  }
  Yk<-c()
  for(i in 1:length(List)){
    Num<-Data_Frame[[2]][i]
    Num<-(as.numeric(Num))
    Yk<-append(Yk,Num)
  }
  plot(Xp, Yk, main=Title,
       xlab=Xlab,
       ylab=Ylab,
       pch=19, cex=1)
}
Drawer_all<-function(specified1="No",specified2="No",Var1=1,Var2=2){
  tango<-Var2-Var1+1
  graphics.off()
  par(mfrow=c(tango,tango),mar=c(1,1,1,1))
  
  for(i in Var1:Var2){
    for(j in Var1:Var2){
      if(i==j){
        plot(1:3)   
        txt<-paste("Var", i, sep="")
        text(x = 2, y = 2,                
             txt,cex = 3)
      }
      else{
        DrawIt(specified1=specified1,specified2=specified2,Var1=j,Var2=i,Title="")
      }
    }
  }
}
#Scale
Scale<-function(var1=4,var2=5,dataframe=DatasetNA){
  list<-ObservationNum(dataframe=DatasetNA,Var1 = var1,Var2 = var2)
  c<-length(list)
  b<-c()
  for(i in 1:c){
    d<-list[[i]]
    unstable <- DatasetNA[[var1+3]][d]
    unstable <- gsub(",",".",unstable)
    unstable <- as.numeric(unstable)
    b<-append(b,unstable)
  }
  b<-sort(b)
  Sum<-0
  for(i in 1:c){
    Sum<-b[i]+Sum
  }
  Mean<-Sum/c
  Standard_deviation<-0
  Deviation_Var2<-0
  for(i in 1:c){
    Deviation_Var1<-b[i]-Mean
    Deviation_Var2<-Deviation_Var1*Deviation_Var1+Deviation_Var2
  }
  Standard_deviation<-sqrt(Deviation_Var2/(c-1))
  scale<-c()
  for(i in 1:c){
    scra<-(b[i]-Mean)/Standard_deviation
    scra<-as.character(scra)
    scale<-append(scale,scra)
  }
  
  return(scale)
}





#===================================!!!!----AFTER YOU'VE RUN FUNCTION ABOVE,USE FUNCTIONS BELOW----!!!!=====================================================================================================
#!!----After you have used the functions below,click on them from "Environment" tab----!!

#Calculate Number of observations
#Change var1 and var2 values to var number as you wish to see. Var1 and Var2 values must be same, For example if you want to see Var4, change code to like this: (Var1=4,Var2=4)
list<-ObservationNum(specified1 = "No",specified2 = "No",Var1 = 7,Var2 = 7)

#Minimum,Maximum,Range,Sum,Mean,Median,Sum of squares,Variance,Standard deviation
#Change var1 and var2 values to var number as you wish to see. Var1 and Var2 values must be same, For example if you want to see Var4, change code to like this: (Var1=4,Var2=4)
Frame<-Calculate(var1=2,var2=2,Specified1 = "No",Specified2 ="No")

#Cross-products,Covariance,Correlations
#You can change Var1(first variable as you want) and Var2(second variable as you want)
#For example: (Var1=4,Var2=5)---> 4 means Var4, 5 means Var5)
Calculated<-Calculate_Second(Var_1=1,Var_2=2,Spec1="No",Spec2="No")




#====BY ONLY FACTOR OF GROUP, ONLY FACTOR OF GENDER AND GROUP BY GENDER FACTOR COMBINATION====
#!!!!----Please enter specified1 as gender you want and specified2 as group you want----!!!!.

#Calculate Number of observations
#Change var1 and var2 values to var number as you wish to see. Var1 and Var2 values must be same, For example if you want to see Var4, change code to like this: (Var1=4,Var2=4)
list<-ObservationNum(specified1 = "Female",specified2 = "Group1",Var1 = 1,Var2 = 1)

#Minimum,Maximum,Range,Sum,Mean,Median,Sum of squares,Variance,Standard deviation
#Change var1 and var2 values to var number as you wish to see. Var1 and Var2 values must be same, For example if you want to see Var4, change code to like this: (Var1=4,Var2=4)
Frame<-Calculate(var1=2,var2=2,Specified1 = "Male",Specified2 ="Group3")

#Cross-products,Covariance,Correlations
#You can change Var1(first variable as you want) and Var2(second variable as you want)
#For example: (Var1=4,Var2=5)---> 4 means Var4, 5 means Var5)
Calculated<-Calculate_Second(Var_1=3,Var_2=4,Spec1="Male",Spec2="Group2")




#========SCATTERPLOT FUNCTION==========
#You can change Var1(first variable as you want) and Var2(second variable as you want)
#For example: (Var1=4,Var2=5)---> 4 means Var4, 5 means Var5)

DrawIt(specified1="No",specified2="No",Var1=1,Var2=2,
       Title="Scatter Plot of 2 Variables",Xlab="Var1",
       Ylab="Var2")
------------------------------------------------------
#You can use this in order to delete scatter plot.
dev.off()



#====================SCATTERPLOT-MATRIX FUNCTION====================
#Please click zoom button and toggle fullscreen for better view after you have run the function.

Drawer_all(specified1="No",specified2="No",Var1=1,Var2=8)
------------------------------------------------------
#You can use this in order to delete scatter plot.
dev.off()


#=========================SCALE=====================================
#You can change Var1(first variable as you want) and Var2(second variable as you want)
#For example: (Var1=4,Var2=5)---> 4 means Var4, 5 means Var5)
#But if you want single Var scale enter parameters like this--> Change var1 and var2 values to var number as you wish to see. Var1 and Var2 values must be same, For example if you want to see Var4, change code to like this: (Var1=4,Var2=4)

print(vec<-Scale(var1=1,var2=1,dataframe=DatasetNA))












