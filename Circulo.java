package Micodigo;

public class Circulo {
	//ATRIBUTOS
	private MiParejaNumeros centroCirculo;
	private double radio;
	
	
	//CONSTRUCTOR
	public Circulo(int coordx, int coordy, double radio) {
		super();
		centroCirculo=new MiParejaNumeros(coordx,coordy);
		this.radio = radio;
		
	}
	
	//METODOS
	public int getCoordx() {
		return centroCirculo.num1;
	}

	public void setCoordx(int coordx) {
		centroCirculo.setNum1(coordx);
	}

	public int getCoordy() {
		return centroCirculo.num2;
	}

	public void setCoordy(int coordy) {
		centroCirculo.setNum2(coordy);
	}

	public double getRadio() {
		return radio;
	}

	public void setRadio(float radio) {
		this.radio = radio;
	}
	
	public double devuelveArea(){
		double area;
		area=Math.PI*Math.pow(radio, 2);
		return area;
	}
	
	public double devuelvelongitud() {
		double longitud;
		longitud=2*Math.PI*radio;
		return longitud;
	}
	
}
