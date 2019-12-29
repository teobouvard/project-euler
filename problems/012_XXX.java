public class Problemn {
	public static void main(String[] args) {
        Integer triangleNumber = 0;
        Integer counter = 0;
        Integer ndivisors = 0;
        while (ndivisors < 50) {
            counter++;
            triangleNumber += counter;
            ndivisors = count_divisors(triangleNumber);
    		//System.out.println(triangleNumber);
        }
		System.out.println(triangleNumber);
	}

    public static Integer count_divisors(Integer n){
        Integer ndivisors = 0;
        for (Integer i = 1; i <= n; i++){
            if (n % i == 0) {
                ndivisors++;
            }
        }
        return ndivisors;
    }
}