package Micodigo;

public class ManejaNumeros {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		MiParejaNumeros objeto1;//declaro el objeto
		objeto1=new MiParejaNumeros(1,2);//Instancio
		objeto1.setNum1(5);
		objeto1.setNum2(5);
		int suma;
		suma=objeto1.devuelveSuma();
		System.out.println("La suma vale");
		System.out.println(suma);
		System.out.println("La resta vale");
		System.out.println(objeto1.devuelveResta());
		
	}

}
