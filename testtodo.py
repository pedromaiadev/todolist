# tests/test_todo.py - Testes unitários do Gerenciador de Tarefas
 
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
 
import todo
 
def setup_function():
    """Limpa a lista de tarefas antes de cada teste."""
    todo.tarefas.clear()
 
 
def test_adicionar_tarefa():
    resultado = todo.adicionar_tarefa("Estudar Python")
    assert resultado == True
    assert len(todo.tarefas) == 1
    assert todo.tarefas[0]["descricao"] == "Estudar Python"
    assert todo.tarefas[0]["concluida"] == False
 
 
def test_adicionar_tarefa_descricao_vazia():
    resultado = todo.adicionar_tarefa("")
    assert resultado == False
    assert len(todo.tarefas) == 0
 
 
def test_adicionar_tarefa_descricao_espacos():
    resultado = todo.adicionar_tarefa("   ")
    assert resultado == False
    assert len(todo.tarefas) == 0
 
def test_concluir_tarefa():
    todo.adicionar_tarefa("Fazer exercícios")
    resultado = todo.concluir_tarefa(1)
    assert resultado == True
    assert todo.tarefas[0]["concluida"] == True
 
 
def test_concluir_tarefa_inexistente():
    resultado = todo.concluir_tarefa(99)
    assert resultado == False
 
 
def test_remover_tarefa():
    todo.adicionar_tarefa("Ler um livro")
    resultado = todo.remover_tarefa(1)
    assert resultado == True
    assert len(todo.tarefas) == 0
 
 
def test_remover_tarefa_inexistente():
    resultado = todo.remover_tarefa(99)
    assert resultado == False
 
 
def test_multiplas_tarefas():
    todo.adicionar_tarefa("Tarefa 1")
    todo.adicionar_tarefa("Tarefa 2")
    todo.adicionar_tarefa("Tarefa 3")
    assert len(todo.tarefas) == 3