package Micodigo;
//CLASE HIJA DE FECHA-- UNA CLASE HIJA NECESITA TENER EN LOS ATIRBUTOS "SUPER"
public class Cumpleaņos extends Fecha {
	//ATRIBUTO
	private String Nombre;
	
	
	//CONSTRUCTOR
	public Cumpleaņos(int dia, int mes, int anio, String Nombre) {
		super(dia, mes, anio);
		// TODO Auto-generated constructor stub
	}
	
	
	//METODOS
	public String getNombre() {
		return Nombre;
	}

	public void setNombre(String Nombre) {
		this.Nombre = Nombre;
	}


	
}
