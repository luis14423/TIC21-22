package Micodigo;

public class ManejaCirculos {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Circulo circulo1;
		Circulo circulo2;
		circulo1=new Circulo(7,9,4.5);
		circulo2=new Circulo(1,2,3);
		
		System.out.println("CIRCULITO 1: ");
		System.out.println("Coordenada x del centro: "+circulo1.getCoordx());
		System.out.println("Coordenada y del centro: "+circulo1.getCoordy());
		System.out.println("Radio: "+circulo1.getRadio());
		System.out.println("Area: "+circulo1.devuelveArea());
		System.out.println("Longitud: "+circulo1.devuelvelongitud());
		
		System.out.println("-----------------------");
		
		System.out.println("CIRCULITO 2: ");
		System.out.println("Coordenada x del centro: "+circulo2.getCoordx());
		System.out.println("Coordenada y del centro: "+circulo2.getCoordy());
		System.out.println("Radio: "+circulo2.getRadio());
		System.out.println("Area: "+circulo2.devuelveArea());
		System.out.println("Longitud: "+circulo2.devuelvelongitud());

		
	}
}
