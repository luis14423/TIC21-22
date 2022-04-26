package Repaso;

public class I1 {
	
	//Atributos
	public String nombre;
	public double radio;
	public int numero;
	
	//Constructor
	
	public I1(String nombre, double radio) {
		super();
		this.nombre = nombre;
		this.radio = radio;
	}

	//Metodos
	public void setNumero(int numero) {
		this.numero= numero;
	}
	
	public int getNumero() {
		return numero;
	}
	public String getNombre() {
		return nombre;
	}


	public void setNombre(String nombre) {
		this.nombre = nombre;
	}


	public double getRadio() {
		return radio;
	}


	public void setRadio(double radio) {
		this.radio = radio;
	}
	
	public double getArea() {
		double x=0;
		x=3.141516*radio;
		return x;
	}
	
	public String getSaludo() {
		String x="";
		x="Buenos dias "+nombre;
		return x;
	}
	
	String esDiv() {
		boolean loEs=false;
		String x="EL numero"+this.getNumero()+" no es divisible entre dos";
		if(this.getNumero()%2==0) {
			loEs=true;
		}
		
		if(loEs==true) {
			x="EL numero "+this.getNumero()+" es divisible entre dos";
		}
		return x;
	}
	
	
	

}
