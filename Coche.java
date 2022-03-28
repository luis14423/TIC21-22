package Micodigo;

public class Coche extends Vehiculo {
    private String marca;
    public Coche(String nombre, String medio) {
        super(nombre, medio);
        //TODO Auto-generated constructor stub
    }
    public String getMarca() {
        return marca;
    }
    public void setMarca(String marca) {
        this.marca = marca;
    }
}
