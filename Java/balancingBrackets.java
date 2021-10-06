public boolean isValid(String s) {

	Deque<Character> stack = new ArrayDeque<>();


	for(Character c : s.toCharArray()) {

		if(stack.isEmpty()){
			stack.push(c);
			continue;
		}

		if(c == '(' || c == '[' || c == '{') 
			stack.push(c);
		else if(c == ')' && stack.peek() == '(')
			stack.pop();
		else if(c == '}' && stack.peek() == '{')
			stack.pop();
		else if(c == ']' && stack.peek() == '[')
			stack.pop();
		else
			return false;
	}

	return stack.isEmpty();
}