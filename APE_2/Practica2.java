import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

public class CajeroAutomatico {

    // Variable compartida
    private static int saldo = 1000;

    // Mutex para proteger el acceso a saldo
    private static final Lock mutexSaldo = new ReentrantLock();

    // Procedimiento de Retiro
    public static void retirar(int id, int cantidad) {
        // Adquirir el mutex antes de consultar o modificar
        mutexSaldo.lock();
        try {
            System.out.println("Proceso " + id + " intenta retirar $" + cantidad);
            if (saldo >= cantidad) {
                // Simula un ligero retardo de procesamiento en la sección crítica
                Thread.sleep(10);
                saldo -= cantidad;
                System.out.println("Proceso " + id + ": Retiro realizado. Saldo actual: $" + saldo);
            } else {
                System.out.println("Proceso " + id + ": Saldo insuficiente. Saldo actual: $" + saldo);
            }
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            // Liberar siempre el mutex en el bloque finally
            mutexSaldo.unlock();
        }
    }

    // Procedimiento de Depósito
    public static void depositar(int id, int cantidad) {
        // Adquirir el mutex antes de consultar o modificar
        mutexSaldo.lock();
        try {
            System.out.println("Proceso " + id + " deposita $" + cantidad);
            // Simula un ligero retardo de procesamiento en la sección crítica
            Thread.sleep(10);
            saldo += cantidad;
            System.out.println("Proceso " + id + ": Depósito realizado. Saldo actual: $" + saldo);
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        } finally {
            // Liberar siempre el mutex en el bloque finally
            mutexSaldo.unlock();
        }
    }

    public static void main(String[] args) {
        // Creación de los tres procesos / hilos
        Thread p1 = new Thread(() -> retirar(1, 300));
        Thread p2 = new Thread(() -> retirar(2, 250));
        Thread p3 = new Thread(() -> depositar(3, 200));

        // Inicio de ejecución concurrente
        p1.start();
        p2.start();
        p3.start();

        // Esperar a que los tres hilos terminen
        try {
            p1.join();
            p2.join();
            p3.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }

        System.out.println("\n--- SALDO FINAL EN LA CUENTA: $" + saldo + " ---");
    }
}