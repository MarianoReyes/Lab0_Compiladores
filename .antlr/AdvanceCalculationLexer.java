// Generated from c:\Users\lp109\OneDrive\Documentos\0lps\01 U\0LaU\000Octavo semestre\Compis\labs\Lab0_Compiladores\AdvanceCalculation.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class AdvanceCalculationLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		DIGITO=1, NEGATIVO=2, PUNTO=3, IGUAL=4, SUMA=5, MULTIPLICACION=6, NUMERO=7, 
		NUMERO_HEXADECIMAL=8, NUMERO_FLOTANTE=9, POTENCIA=10, NUMERO_POTENCIADO=11, 
		WS=12;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"DIGITO", "NEGATIVO", "PUNTO", "IGUAL", "SUMA", "MULTIPLICACION", "NUMERO", 
			"NUMERO_HEXADECIMAL", "NUMERO_FLOTANTE", "POTENCIA", "NUMERO_POTENCIADO", 
			"WS"
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


	public AdvanceCalculationLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "AdvanceCalculation.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16\\\b\1\4\2\t\2"+
		"\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7"+
		"\3\b\5\b)\n\b\3\b\6\b,\n\b\r\b\16\b-\3\t\3\t\6\t\62\n\t\r\t\16\t\63\3"+
		"\n\6\n\67\n\n\r\n\16\n8\3\n\3\n\6\n=\n\n\r\n\16\n>\3\13\3\13\3\f\6\fD"+
		"\n\f\r\f\16\fE\3\f\3\f\6\fJ\n\f\r\f\16\fK\5\fN\n\f\3\f\3\f\6\fR\n\f\r"+
		"\f\16\fS\3\r\6\rW\n\r\r\r\16\rX\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13\7\r"+
		"\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\3\2\62;\4\2CHch\5\2\13\f\17\17"+
		"\"\"\2f\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2"+
		"\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3"+
		"\2\2\2\2\31\3\2\2\2\3\33\3\2\2\2\5\35\3\2\2\2\7\37\3\2\2\2\t!\3\2\2\2"+
		"\13#\3\2\2\2\r%\3\2\2\2\17(\3\2\2\2\21\61\3\2\2\2\23\66\3\2\2\2\25@\3"+
		"\2\2\2\27C\3\2\2\2\31V\3\2\2\2\33\34\t\2\2\2\34\4\3\2\2\2\35\36\7/\2\2"+
		"\36\6\3\2\2\2\37 \7\60\2\2 \b\3\2\2\2!\"\7?\2\2\"\n\3\2\2\2#$\7-\2\2$"+
		"\f\3\2\2\2%&\7,\2\2&\16\3\2\2\2\')\5\5\3\2(\'\3\2\2\2()\3\2\2\2)+\3\2"+
		"\2\2*,\5\3\2\2+*\3\2\2\2,-\3\2\2\2-+\3\2\2\2-.\3\2\2\2.\20\3\2\2\2/\62"+
		"\5\3\2\2\60\62\t\3\2\2\61/\3\2\2\2\61\60\3\2\2\2\62\63\3\2\2\2\63\61\3"+
		"\2\2\2\63\64\3\2\2\2\64\22\3\2\2\2\65\67\5\3\2\2\66\65\3\2\2\2\678\3\2"+
		"\2\28\66\3\2\2\289\3\2\2\29:\3\2\2\2:<\5\7\4\2;=\5\3\2\2<;\3\2\2\2=>\3"+
		"\2\2\2><\3\2\2\2>?\3\2\2\2?\24\3\2\2\2@A\7`\2\2A\26\3\2\2\2BD\5\3\2\2"+
		"CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF\3\2\2\2FM\3\2\2\2GI\5\7\4\2HJ\5\3\2\2"+
		"IH\3\2\2\2JK\3\2\2\2KI\3\2\2\2KL\3\2\2\2LN\3\2\2\2MG\3\2\2\2MN\3\2\2\2"+
		"NO\3\2\2\2OQ\5\25\13\2PR\5\3\2\2QP\3\2\2\2RS\3\2\2\2SQ\3\2\2\2ST\3\2\2"+
		"\2T\30\3\2\2\2UW\t\4\2\2VU\3\2\2\2WX\3\2\2\2XV\3\2\2\2XY\3\2\2\2YZ\3\2"+
		"\2\2Z[\b\r\2\2[\32\3\2\2\2\16\2(-\61\638>EKMSX\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}