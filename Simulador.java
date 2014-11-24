import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;

public class Simulador {
	static final int QNTSLOTS = 64, SCHOUTE=0;
	static int qntTags, qntSlots = QNTSLOTS, qntColisoes = 0,
			qntSucessos = 0, qntVazios = 0, qntTotais = qntSlots, qntTotaisColisoes = 0;
	static int[] slots = new int[qntSlots];
	static boolean cont = true;

	public static void leitura(int method) {
		Random random = new Random();
		for (int i = 0; i < qntTags; i++) {
			int a = random.nextInt(qntSlots);
			slots[a]++;
		}
		for (int i = 0; i < qntSlots; i++) {
			if (slots[i] == 0) {
				qntVazios++;
			} else if (slots[i] == 1) {
				qntSucessos++;
				qntTags--;
			} else {
				qntColisoes++;
			}

			slots[i] = 0;
		}
		qntTotaisColisoes += qntColisoes;
		if (qntColisoes > 0) {
			if(method == SCHOUTE)qntSlots = schoute();//mudar so o metodo de calcular
			qntTotais += qntSlots;
			qntSucessos = qntColisoes = 0;
			if (qntSlots > slots.length) {
				slots = new int[qntSlots];
			}
		} else {
			cont = false;
		}
	}
	
	private static void gravar(StringBuffer impressao, File f) throws IOException {
		BufferedWriter bw = null;
		FileWriter fw = null;
		try {
			fw = new FileWriter(f);
			bw = new BufferedWriter(fw);
			bw.write(impressao.toString());
		} catch (IOException e) {
			e.printStackTrace();
		} finally {
			bw.close();
			fw.close();
		}
	}
	
	private static int schoute(){
		return (int) Math.ceil(2.39 * qntColisoes);
	}
	
	public static void main(String[] args){
		String name = args[0];
		int method = -1;
		if(name.equalsIgnoreCase("schoute"))method = SCHOUTE;
		else {
			System.err.println("Invalid method");
			System.exit(1);
		}
		for(int qnt_tags = 100;qnt_tags<=1001;qnt_tags+=100){
			File f = new File(name+qnt_tags+".csv");
			int contador = 1;
			StringBuffer impressao = new StringBuffer();
			while (contador <= 1000) {
				while (cont) {
					leitura(method);
				}
				String toAppend = qntTotais + "," + qntVazios + "," + qntTotaisColisoes + "\r\n";
				impressao.append(toAppend);
				contador++;
				qntTags = qnt_tags;
				qntSlots = qntTotais = QNTSLOTS;
				qntColisoes = qntSucessos = qntVazios = qntTotaisColisoes = 0;
				cont = true;
			}
			try {
				gravar(impressao, f);
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
	}
}