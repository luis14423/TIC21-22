package Micodigo;

public class CocheElectrico extends Coche {
	private double potencia;
	

	public CocheElectrico(String nombre, String medio) {
		super(nombre, medio);
	    //TODO Auto-generated constructor stub
	    }


	public double getPotencia() {
		return potencia;
	}
	public void setPotencia(double potencia) {
		this.potencia = potencia;
	}

}
