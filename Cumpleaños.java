package Micodigo;
//CLASE HIJA DE FECHA-- UNA CLASE HIJA NECESITA TENER EN LOS ATIRBUTOS "SUPER"
public class Cumplea�os extends Fecha {
	//ATRIBUTO
	private String Nombre;
	
	
	//CONSTRUCTOR
	public Cumplea�os(int dia, int mes, int anio, String Nombre) {
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
