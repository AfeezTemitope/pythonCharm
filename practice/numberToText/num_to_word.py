import inflect

def main():
    p = inflect.engine()
    try:
        user_input = int(input("Enter a number: "))
        if user_input < 0:
            print("Please enter a positive number.")
        else:
            num_in_words = p.number_to_words(user_input)
            print(f"Number in words: {num_in_words}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()




#     import java.util.Scanner;
#
# public class Main {
# public static void main(String[] args) {
# Scanner scanner = new Scanner(System.in);
# System.out.print("Enter a number: ");
# try {
# long user_input = scanner.nextLong();
# if (user_input < 0) {
# System.out.println("Please enter a positive number.");
# } else {
# String num_in_words = convertToWords(user_input);
# System.out.println("Number in words: " + num_in_words);
# }
# } catch (java.util.InputMismatchException e) {
# System.out.println("Invalid input. Please enter a valid integer.");
# }
# }
#
# private static String convertToWords(long number) {
# if (number == 0) {
# return "zero";
# }
#
# String[] units = {
# "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
# "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
# };
#
# String[] tens = {
# "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
# };
#
# String[] thousands = {"", "thousand", "million", "billion"};
#
# StringBuilder result = new StringBuilder();
#
# for (int i = 3; i >= 0; i--) {
# long divisor = (long) Math.pow(10, 3 * i);
# if (number >= divisor) {
# long chunk = number / divisor;
# number %= divisor;
#
# if (chunk > 0) {
# String chunkWords = convertToWords(chunk);
# result.append(chunkWords).append(" ").append(thousands[i]);
# if (number > 0) {
# result.append(" ");
# }
# }
# }
# }
#
# if (number > 0) {
# if (result.length() > 0) {
# result.append("and ");
# }
# if (number < 20) {
# result.append(units[(int) number]);
# } else {
# result.append(tens[(int) (number / 10)]);
# if (number % 10 > 0) {
# result.append("-").append(units[(int) (number % 10)]);
# }
# }
# }
#
# return result.toString();
# }
# }

