import java.io.*;
import java.net.*;
import java.util.Scanner;

public class TCPClient {
    private Socket socket;
    private PrintWriter out;
    private BufferedReader in;

    public TCPClient(String address, int port) {
        try {
            socket = new Socket(address, port);
            out = new PrintWriter(socket.getOutputStream(), true);
            in = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            System.out.println("Connected to the server");
            
            new Thread(new ReceiveMessages()).start();
            sendMessages();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private void sendMessages() {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            String message = scanner.nextLine();
            out.println(message);
        }
    }

    private class ReceiveMessages implements Runnable {
        @Override
        public void run() {
            String message;
            try {
                while ((message = in.readLine()) != null) {
                    System.out.println("Received: " + message);
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        new TCPClient("127.0.0.1", 65432);
    }
}
