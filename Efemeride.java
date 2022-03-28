package Micodigo;
//CLASE HIJA DE FECHA-- UNA CLASE HIJA NECESITA TENER EN LOS ATIRBUTOS "SUPER"
public class Efemeride extends Fecha {
	
	//ATRIBUTO
	private String quePaso;
	
	
	//CONSTRUCTOR
	public Efemeride(int dia, int mes, int anio, String quePaso) {
		super(dia,mes,anio);
		//TODO Auto-generated constructor stub
		this.setQuePaso(quePaso);
		}

	//METODOS
	public String getQuePaso() {
		return quePaso;
	}

	public void setQuePaso(String quePaso) {
		this.quePaso = quePaso;
	}

}
