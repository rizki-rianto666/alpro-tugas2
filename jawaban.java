//Tipe Data Integer
public class Integer {
  public static void main (String [] args){
    byte nilai_byte = 127;
    short nilai_short = 32767;
    int nilai_int = 2147483647;
    long nilai_long = 9000000000L;
    
    System.out.println("Integer merupakan tipe data yang bernilai angka bilangan bulat, berikut tipe data bilangan bulat dan contoh nya :");
    System.out.println("Nilai dari tipe data byte = " + nilai_byte);
    System.out.println("Nilai dari tipe data short = " + nilai_short);
    System.out.println("Nilai dari tipe data int = " + nilai_int);
    System.out.println("Nilai dari tipe data long = " + nilai_long);
  }
}

//Floating Point (Desimal)
public class Floating {
    public static void main (String[]args) {
        float nilai_float = 2.44f;
        double nilai_double = 2.12345678910d;

        System.out.println("Floating point merupakan bilangan desimal. Pada tipe data ini ada 2, yaitu Float dan Double");
        System.out.println("Float untuk 6-7 desimal dan berukuran 32 bit, sedangkan Double untuk hingga 15 digit desimal dan ukurannya 64bit");
        System.out.println("===================");
        System.out.println("Contoh nilai float = " + nilai_float);
        System.out.println("Contoh nilai double = " + nilai_double);
        
    }
}


//Karakter (Char)
public class Char{
    public static void main (String[]args){
        char char_A = 'A';
        char char_B = 'B';

        System.out.println("Nilai char_A = " + char_A);
        System.out.println("Nilai char_B = " + char_B);
    }

}


//Boolean
public class Boolean {
    public static void main(String[] args) {
        boolean Life_Exist = true;
        boolean Life_Doesnt_Exist = false;
        System.out.println("Boolean merupakan tipe data True - False, biasanya digunakan untuk menyatakan suatu hal/kondisi bernilai Benar atau Salah");
        System.out.println("======= Contoh =======");
        System.out.println("Nilai Boolean dari Life_Exist = " + Life_Exist);
        System.out.println("Nilai Boolean dari Life_Doesnt_Exist = " + Life_Doesnt_Exist);
}
}


// String
public class Setring {
  public static void main(String[] args) {
    String myString = "Hi There ! Saya hengkel --Contoh String di variabel myString";
    System.out.println(myString);
  }
}
