// Generated from c:\Users\lp109\OneDrive\Documentos\0lps\01 U\0LaU\000Octavo semestre\Compis\labs\Lab0_Compiladores\AdvanceCalculation.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AdvanceCalculationParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DIGITO=1, NEGATIVO=2, PUNTO=3, IGUAL=4, SUMA=5, MULTIPLICACION=6, NUMERO=7, 
		NUMERO_HEXADECIMAL=8, NUMERO_FLOTANTE=9, POTENCIA=10, NUMERO_POTENCIADO=11, 
		WS=12;
	public static final int
		RULE_okens = 0;
	private static String[] makeRuleNames() {
		return new String[] {
			"okens"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, null, "'-'", "'.'", "'='", "'+'", "'*'", null, null, null, "'^'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "DIGITO", "NEGATIVO", "PUNTO", "IGUAL", "SUMA", "MULTIPLICACION", 
			"NUMERO", "NUMERO_HEXADECIMAL", "NUMERO_FLOTANTE", "POTENCIA", "NUMERO_POTENCIADO", 
			"WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "AdvanceCalculation.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public AdvanceCalculationParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class OkensContext extends ParserRuleContext {
		public TerminalNode DIGITO() { return getToken(AdvanceCalculationParser.DIGITO, 0); }
		public TerminalNode PUNTO() { return getToken(AdvanceCalculationParser.PUNTO, 0); }
		public TerminalNode NUMERO() { return getToken(AdvanceCalculationParser.NUMERO, 0); }
		public TerminalNode POTENCIA() { return getToken(AdvanceCalculationParser.POTENCIA, 0); }
		public TerminalNode NUMERO_POTENCIADO() { return getToken(AdvanceCalculationParser.NUMERO_POTENCIADO, 0); }
		public TerminalNode NUMERO_HEXADECIMAL() { return getToken(AdvanceCalculationParser.NUMERO_HEXADECIMAL, 0); }
		public TerminalNode NUMERO_FLOTANTE() { return getToken(AdvanceCalculationParser.NUMERO_FLOTANTE, 0); }
		public TerminalNode NEGATIVO() { return getToken(AdvanceCalculationParser.NEGATIVO, 0); }
		public TerminalNode IGUAL() { return getToken(AdvanceCalculationParser.IGUAL, 0); }
		public TerminalNode SUMA() { return getToken(AdvanceCalculationParser.SUMA, 0); }
		public TerminalNode MULTIPLICACION() { return getToken(AdvanceCalculationParser.MULTIPLICACION, 0); }
		public OkensContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_okens; }
	}

	public final OkensContext okens() throws RecognitionException {
		OkensContext _localctx = new OkensContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_okens);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(2);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << DIGITO) | (1L << NEGATIVO) | (1L << PUNTO) | (1L << IGUAL) | (1L << SUMA) | (1L << MULTIPLICACION) | (1L << NUMERO) | (1L << NUMERO_HEXADECIMAL) | (1L << NUMERO_FLOTANTE) | (1L << POTENCIA) | (1L << NUMERO_POTENCIADO))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16\7\4\2\t\2\3\2"+
		"\3\2\3\2\2\2\3\2\2\3\3\2\3\r\2\5\2\4\3\2\2\2\4\5\t\2\2\2\5\3\3\2\2\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}