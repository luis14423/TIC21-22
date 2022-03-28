package Micodigo;

public class Vehiculo {
	//ATRIBUTOS
	private String nombre;
	private String medio;
	private double velocidad;
	private int capacidad;
	private int ruedas;
	private int puertas;
	
	//CONSTRUCTOR
	public Vehiculo(String nombre,String medio) {
		super();
		this.nombre=nombre;
		this.medio = medio;
		
	}

	
	//METODOS
	public String getnombre() {
		return nombre;
	}
	
	public void setnombre(String nombre) {
		this.nombre=nombre;
	}
	
	public String getMedio() {
		return medio;
	}

	public void setMedio(String medio) {
		this.medio = medio;
	}

	public double getVelocidad() {
		return velocidad;
	}

	public void setVelocidad(double velocidad) {
		this.velocidad = velocidad;
	}

	public int getCapacidad() {
		return capacidad;
	}

	public void setCapacidad(int capacidad) {
		this.capacidad = capacidad;
	}

	public int getRuedas() {
		return ruedas;
	}

	public void setRuedas(int ruedas) {
		this.ruedas = ruedas;
	}

	public int getPuertas() {
		return puertas;
	}

	public void setPuertas(int puertas) {
		this.puertas = puertas;
	}
	
}
