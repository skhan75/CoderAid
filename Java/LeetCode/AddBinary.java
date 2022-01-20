class AddBinary {
    public String addBinary(String a, String b) {
        int n = a.length(),
                m = b.length();

        if (n < m)
            return addBinary(b, a);

        int L = Math.max(a.length(), b.length());

        int carry = 0;
        int j = m - 1;
        StringBuilder sb = new StringBuilder();

        for (int i = L - 1; i >= 0; i--) {
            if (a.charAt(i) == '1')
                carry++;
            if (j > -1 && b.charAt(j--) == '1')
                carry++;

            if (carry % 2 == 0)
                sb.append('0');
            else
                sb.append('1');

            carry = carry / 2;
        }

        if (carry == 1)
            sb.append('1');

        return sb.reverse().toString();
    }
}

