from flask import Flask, url_for,render_template,request,abort
import math, random
import pandas as pd
import numpy as np
app = Flask(__name__)

# Creating simple Routes 
@app.route('/test')
def test():
    return "Home Page"

@app.route('/test/about/')
def about_test():
    return "About Page"

@app.route('/test/mcm/')
def mcm_test():
    return "mcm Page"
# Routes to Render Something
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about', strict_slashes=False)
def about():
    return render_template("about.html")

@app.route('/info', strict_slashes=False)
def info():
    return render_template("info.html")

@app.route('/mrandom', strict_slashes=False)
def mrandom():
    return render_template("mrandom.html")

@app.route('/mprobabilidad', strict_slashes=False)
def mprobabilidad():
    return render_template("mprobabilidad.html")
@app.route('/mregresion', strict_slashes=False)
def mregresion():
    return render_template("mregresion.html")
@app.route('/msimulacion', strict_slashes=False)
def msimulacion():
    return render_template("msimulacion.html")
@app.route('/modsim', strict_slashes=False)
def modsim():
    return render_template("modsim.html")
@app.route('/ae', strict_slashes=False)
def ae():
    return render_template("ae.html")
@app.route('/regre', strict_slashes=False)
def regre():
    return render_template("regre.html")
@app.route('/regreno', strict_slashes=False)
def regreno():
    return render_template("regreno.html")
@app.route('/monte', strict_slashes=False)
def monte():
    return render_template("monte.html")
@app.route('/mti', strict_slashes=False)
def mti():
    return render_template("mti.html")


												# Metodo Cuadrado Medio
@app.route("/mcm",methods=["GET","POST"])
def mcm():
	if request.method=="GET":
		return render_template("mcm.html")
	else:
		try:
			l=len(str(None))
			lista=[]
			lista2=[]
			lista3=[]
			i=0
			num1=int(request.form["num1"])
			num2=int(request.form["num2"])
			
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="cuadradomedio" and lista2!=0:
			while i < num2:
				x=str(num1*num1)
				if l % 2 == 0:
					x=x.zfill(l*2)
				else:
					x=x.zfill(l)
				y=(len(x)-l)/2
				y=int(y)
				num1=int(x[y:y+l])
				lista.append(num1)
				lista2.append(x)
				lista3.append(num1/10000)
				i=i+1
						

		else:
			abort(404)
				
		return render_template("mcm.html",numero1=num1,numero2=num2,operacion=op,lista2=lista2,lista=lista,lista3=lista3)

			
				
				
                                              # Metodo Confruencial Adictivo
@app.route("/mca",methods=["GET","POST"])
def mca():
	if request.method=="GET":
		return render_template("mca.html")
	else:
		try:
			num1=int(request.form["num1"]) # N
			num2=int(request.form["num2"]) # M
			num3=int(request.form["num3"]) # A
			num4=int(request.form["num4"]) # X0
			num5=int(request.form["num5"]) # C
			
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="congruencialaditivo" :
			x=[1]*num1
			r=[0.1]*num1
			xn=[1]*num1
			axn=[1]*num1
			for i in range(0,num1):
				xn[i]=((num3*num4)+num5)
				axn[i]=round(xn[i]/num3,1)
				x[i]=((num3*num4)+num5)%num2
				num4=x[i]
				r[i]=num4/num2
				
		else:
			abort(404)
		return render_template("mca.html",numero1=num1,numero2=num2,numero3=num3,numero4=num4,numero5=num5,operacion=op,x=x,r=r,xn=xn,axn=axn)


                                              # Metodo Confruencial Multiplicativo
@app.route("/mcmu",methods=["GET","POST"])
def mcmu():
	if request.method=="GET":
		return render_template("mcmu.html")
	else:
		try:
			num1=int(request.form["num1"]) # N
			num2=int(request.form["num2"]) # M
			num3=int(request.form["num3"]) # A
			num4=int(request.form["num4"]) # X0
			
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="congruencialmultiplicativo" :
			x=[1]*num1
			r=[0.1]*num1
			xn=[1]*num1
			axn=[1]*num1
			for i in range(0,num1):
				xn[i]=(num3*num4)
				axn[i]=(xn[i]/num3)
				x[i]=(num3*num4)%num2
				num4=x[i]
				r[i]=num4/num2		    
		else:
			abort(404)
		return render_template("mcmu.html",numero1=num1,numero2=num2,numero3=num3,numero4=num4,operacion=op,x=x,r=r,xn=xn,axn=axn)

                                                # M . Programacion Movil
@app.route("/pm",methods=["GET","POST"])
def pm():
	if request.method=="GET":
		return render_template("pm.html")
	else:
		try:
			num1=int(request.form["nochapter"]) # Generar muestra

			
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="promediomovil" :
			x=[1]*num1
			r=num1
			
			
					    
		else:
			abort(404)
		return render_template("pm.html",numero1=num1,operacion=op,x=x,r=r)

@app.route("/pm",methods=["GET","POST"])
def modelo():
	if request.method=="GET":
		return render_template("pm.html")
	else:
		try:
			num1=int(request.form["nochapter"]) # Generar muestra

			
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="promediomovil" :
			x=[1]*num1
			r=num1
			
			
					    
		else:
			abort(404)
		return render_template("pm.html",numero1=num1,operacion=op,x=x,r=r)
				
				
                                              # Metodo Linea de Espera
@app.route("/mle",methods=["GET","POST"])
def mle():
	if request.method=="GET":
		return render_template("mle.html")
	else:
		try:
			num1=int(request.form["num1"]) # N
			num6=float(request.form["num6"]) # L
			num7=int(request.form["num7"]) # MIU
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="congruencialadictivo" :
			landa=num6
			n=num7
			p=round(num6/num7,3)*1
			po=round(1.0-(num6/num7),3)
			lq=round(num6*num6/(num7*(num7-num6)),3)
			l=round(num6/(num7-num6),3)
			w=round(1/(num7-num6),3)
			wq=round(w-(1.0/num7),3)
			pn=round((num6/num7)*1*po,3)
			x=[1]*num1
			r=[0.1]*num1
			r2=[0.1]*num1
			xn=[1]*num1
			axn=[1]*num1
			tell=[1]*num1
			ts=[1]*num1
			hll=[0]*num1
			his=[0.1]*num1
			tfs=[0]*num1
			tee=[1]*num1
			tes=[1]*num1
			for i in range(0,num1):
				r[i]=round(random.random(),2)
				r2[i]=round(random.random(),2)
				tell[i]=round((-landa*np.log(r[i])),2)
				ts[i]=round((-n*np.log(r2[i])),2)
				hll[i]=round((tell[i]+hll[i-1]),2)
				his[i]=round(max(hll[i],tfs[i-1]),2)
				tfs[i]=round((his[i]+ts[i]),2)
				tee[i]=round((his[i]-hll[i]),2)
				tes[i]=round((tee[i]+ts[i]),2)
		else:
			abort(404)
		return render_template("mle.html",numero1=num1,numero6=num6,numero7=num7,operacion=op,p=p,po=po,lq=lq,landa=landa,n=n,l=l,w=w,wq=wq,pn=pn,x=x,r=r,r2=r2,xn=xn,axn=axn,tell=tell,ts=ts,hll=hll,his=his,tfs=tfs,tee=tee,tes=tes)

													# Metodo Linea de Espera
@app.route("/mle2",methods=["GET","POST"])
def mle2():
	if request.method=="GET":
		return render_template("mle2.html")
	else:
		try:
			num1=int(request.form["num1"]) # N
			num6=float(request.form["num6"]) # L
			num7=int(request.form["num7"]) # MIU
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="congruencialadictivo" :
			nuit=num1
			landa=num6
			n=num7
			p=round(num6/num7,3)*1
			po=round(1.0-(num6/num7),3)
			lq=round(num6*num6/(num7*(num7-num6)),3)
			l=round(num6/(num7-num6),3)
			w=round(1/(num7-num6),3)
			wq=round(w-(1.0/num7),3)
			pn=round((num6/num7)*1*po,3)
			x=[1]*num1
			r=[0.1]*num1
			r2=[0.1]*num1
			xn=[1]*num1
			axn=[1]*num1
			tell=[1]*num1
			ts=[1]*num1
			hll=[0]*num1
			his=[0.1]*num1
			tfs=[0]*num1
			his2=[0]*num1
			tfs2=[0]*num1
			tee=[1]*num1
			tes=[1]*num1
			csu=[0]*num1
			for i in range(0,num1):
				r[i]=round(random.random(),2)
				r2[i]=round(random.random(),2)
				tell[i]=round((-landa*np.log(r[i])),2)
				ts[i]=round((-n*np.log(r2[i])),2)
				hll[i]=round((tell[i]+hll[i-1]),2)
				csu[i]
				if tfs[i-1]<=his2[i-1]:
					csu[i]=1
				else:
					csu[i]=2
			
				his[i]
				if csu[i]==1:
					his[i]=round(max(hll[i],tfs[i-1]),2)
				else:
					his[i]=round((his[i-1]),2)				
				
				tfs[i]
				if csu[i]==1:
					tfs[i]=round((his[i]+ts[i]),2)
				else:
					tfs[i]=round(tfs[i-1],2)

				his2[i]
				if csu[i]==2:
					his2[i]=round(max(hll[i],tfs2[i-1]),2)
				else:
					his2[i]=round((his2[i-1]),2)
					
				tfs2[i]
				if csu[i]==2:
					tfs2[i]=round((his2[i]+ts[i]),2)
				else:
					tfs2[i]=round(tfs2[i-1],2)
				
				tee[i]
				if csu[i]==1:
					tee[i]=round((his[i]-hll[i]),2)
				else:
					tee[i]=round((his2[i]-hll[i]),2)
				tes[i]=round((tee[i]+ts[i]),2)

				

		else:
			abort(404)
		return render_template("mle2.html",numero1=num1,numero6=num6,
											numero7=num7,operacion=op,p=p,po=po,lq=lq,
											landa=landa,n=n,l=l,w=w,wq=wq,pn=pn,x=x,r=r,
											r2=r2,xn=xn,axn=axn,tell=tell,ts=ts,hll=hll,
											his=his,tfs=tfs,his2=his2,tfs2=tfs2,tee=tee,
											tes=tes,csu=csu,nuit=nuit)

@app.route("/mle3",methods=["GET","POST"])
def mle3():
	if request.method=="GET":
		return render_template("mle3.html")
	else:
		try:
			num1=int(request.form["num1"]) # N
			num2=int(request.form["num2"]) # M
			num3=int(request.form["num3"]) # A
			num4=int(request.form["num4"]) # X0
			num5=int(request.form["num5"]) # C
			num6=float(request.form["num6"]) # L
			num7=int(request.form["num7"]) # MIU
			
		except:
			abort(404)
		op=request.form["operacion"]

		if op=="congruencialadictivo" :
			landa=num6
			n=num7
			nuit=num1
			m=num2
			a=num3
			xo=num4
			c=num5
			p=round(num6/num7,3)*1
			po=round(1.0-(num6/num7),3)
			lq=round(num6*num6/(num7*(num7-num6)),3)
			l=round(num6/(num7-num6),3)
			w=round(1/(num7-num6),3)
			wq=round(w-(1.0/num7),3)
			pn=round((num6/num7)*1*po,3)
			x=[1]*num1
			r=[0.1]*num1
			xn=[1]*num1
			axn=[1]*num1
			r2=[0.1]*num1
			r2=[0.1]*num1
			tell=[1]*num1
			ts=[1]*num1
			hll=[0]*num1
			his=[0.1]*num1
			tfs=[0]*num1
			his2=[0]*num1
			tfs2=[0]*num1
			tee=[1]*num1
			tes=[1]*num1
			csu=[0]*num1
			for i in range(0,num1):
				xn[i]=((num3*num4)+num5)
				axn[i]=round(xn[i]/num3,1)
				x[i]=((num3*num4)+num5)%num2
				num4=x[i]
				r[i]=round(random.random(),2)
				r2[i]=round((num4/num2),2)
				tell[i]=round((-landa*np.log(r[i])),2)
				ts[i]=round((-n*np.log(r2[i])),2)
				hll[i]=round((tell[i]+hll[i-1]),2)
				csu[i]
				if tfs[i-1]<=his2[i-1]:
					csu[i]=1
				else:
					csu[i]=2
			
				his[i]
				if csu[i]==1:
					his[i]=round(max(hll[i],tfs[i-1]),2)
				else:
					his[i]=round((his[i-1]),2)				
				
				tfs[i]
				if csu[i]==1:
					tfs[i]=round((his[i]+ts[i]),2)
				else:
					tfs[i]=round(tfs[i-1],2)

				his2[i]
				if csu[i]==2:
					his2[i]=round(max(hll[i],tfs2[i-1]),2)
				else:
					his2[i]=round((his2[i-1]),2)
					
				tfs2[i]
				if csu[i]==2:
					tfs2[i]=round((his2[i]+ts[i]),2)
				else:
					tfs2[i]=round(tfs2[i-1],2)
				
				tee[i]
				if csu[i]==1:
					tee[i]=round((his[i]-hll[i]),2)
				else:
					tee[i]=round((his2[i]-hll[i]),2)
				tes[i]=round((tee[i]+ts[i]),2)
				
				
		else:
			abort(404)
		return render_template("mle3.html",numero1=num1,numero2=num2,numero3=num3,numero4=num4,
											numero5=num5,operacion=op,p=p,po=po,x=x,r=r,xn=xn,
											lq=lq,l=l,wq=wq,w=w,landa=landa,pn=pn,axn=axn,r2=r2,
											tell=tell,ts=ts,hll=hll,n=n,
											his=his,tfs=tfs,his2=his2,tfs2=tfs2,tee=tee,
											tes=tes,csu=csu,nuit=nuit,m=m,a=a,xo=xo,c=c)




# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)
