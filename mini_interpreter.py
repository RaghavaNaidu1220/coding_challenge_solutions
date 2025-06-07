#!/usr/bin/env python3
"""
mini_interpreter.py:
A minimalist interpreter supporting:
  - "let" variable declarations (e.g., let x = 5)
  - Arithmetic expressions using operators (+, -, *, /)
  - Simple if statements in the form: if <condition> then <statement> [else <statement>]
"""

import re

class MiniInterpreter:
    def __init__(self):
        self.env = {}

    def parse_expression(self, expr):
        """
        Parses and evaluates an arithmetic or boolean expression.
        It replaces variable names with values from the internal environment.
        """
        # Tokenize the expression: variable names, numbers, and operators.
        tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*|\d+|[+\-*/()<>!=]=?|[<>]", expr)
        expr_replaced = ""
        for token in tokens:
            if re.match(r"[A-Za-z_][A-Za-z0-9_]*", token) and token in self.env:
                expr_replaced += str(self.env[token])
            else:
                expr_replaced += token
        try:
            return eval(expr_replaced)
        except Exception:
            raise Exception("Invalid expression: " + expr)

    def interpret_line(self, line):
        """
        Interprets a single line of code.
        Supported:
          - Let declarations: let variable = expression
          - If statements: if <condition> then <statement> [else <statement>]
          - Bare expressions are evaluated.
        """
        line = line.strip()
        if line.startswith("let "):
            # Process variable declaration.
            match = re.match(r"let\s+([A-Za-z_][A-Za-z0-9_]*)\s*=\s*(.+)", line)
            if not match:
                raise Exception("Invalid let declaration: " + line)
            var, expr = match.group(1), match.group(2)
            value = self.parse_expression(expr)
            self.env[var] = value
            return f"{var} = {value}"
        elif line.startswith("if "):
            # Process if statement.
            match = re.match(r"if\s+(.+?)\s+then\s+(.+?)(?:\s+else\s+(.+))?$", line)
            if not match:
                raise Exception("Invalid if statement: " + line)
            condition_expr, then_stmt, else_stmt = match.group(1), match.group(2), match.group(3)
            condition_value = self.parse_expression(condition_expr)
            if condition_value:
                return self.interpret_line(then_stmt)
            elif else_stmt:
                return self.interpret_line(else_stmt)
            else:
                return None
        else:
            # Evaluate a bare expression.
            return self.parse_expression(line)

    def interpret(self, code):
        """
        Processes multiple lines of code.
        
        Parameters:
          code: Multiline string containing the program.
          
        Returns:
          List of outputs from each statement that yields a result.
        """
        results = []
        for line in code.strip().splitlines():
            if not line.strip():
                continue
            result = self.interpret_line(line)
            if result is not None:
                results.append(result)
        return results



code = """
let x = 5
let y = x + 3
if y > 7 then let z = y * 2 else let z = y - 2
z + 10
"""
interpreter = MiniInterpreter()
results = interpreter.interpret(code)
print("Interpreter Results:")
for res in results:
    print(res)


