package Micodigo;

public class Persona {
	//ATRIBUTOS
	String primerApellido;
	String segundoApellido;
	String nombre;
	
	//CONSTRUCTOR
	public Persona (String primerApellido, String segundoApellido, String nombre) {
		this.primerApellido=primerApellido;
		this.segundoApellido=segundoApellido;
		this.nombre=nombre;
	}

	

	
	//METODOS
	public String getPrimerApellido() {
		return primerApellido;
	}

	public void setPrimerApellido(String primerApellido) {
		this.primerApellido = primerApellido;
	}

	public String getSegundoApellido() {
		return segundoApellido;
	}

	public void setSegundoApellido(String segundoApellido) {
		this.segundoApellido = segundoApellido;
	}

	public String getNombre() {
		return nombre;
	}

	public void setNombre(String nombre) {
		this.nombre = nombre;
	}
	
}
