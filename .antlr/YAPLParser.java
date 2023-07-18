// Generated from c:\Users\lp109\OneDrive\Documentos\0lps\01 U\0LaU\000Octavo semestre\Compis\labs\Lab0_Compiladores\YAPL.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, ID=35, INT=36, STRING=37, WS=38;
	public static final int
		RULE_program = 0, RULE_classDeclaration = 1, RULE_feature = 2, RULE_formalParameter = 3, 
		RULE_type = 4, RULE_expression = 5;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "classDeclaration", "feature", "formalParameter", "type", 
			"expression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'class'", "'inherits'", "'{'", "'}'", "':'", "';'", "'('", "','", 
			"')'", "'SELF_TYPE'", "'if'", "'then'", "'else'", "'fi'", "'while'", 
			"'loop'", "'pool'", "'let'", "'<-'", "'in'", "'new'", "'isvoid'", "'.'", 
			"'@'", "'<'", "'<='", "'='", "'+'", "'-'", "'*'", "'/'", "'~'", "'true'", 
			"'false'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, "ID", 
			"INT", "STRING", "WS"
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
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(YAPLParser.EOF, 0); }
		public List<ClassDeclarationContext> classDeclaration() {
			return getRuleContexts(ClassDeclarationContext.class);
		}
		public ClassDeclarationContext classDeclaration(int i) {
			return getRuleContext(ClassDeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(13); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(12);
				classDeclaration();
				}
				}
				setState(15); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__0 );
			setState(17);
			match(EOF);
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

	public static class ClassDeclarationContext extends ParserRuleContext {
		public List<TerminalNode> ID() { return getTokens(YAPLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(YAPLParser.ID, i);
		}
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public ClassDeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_classDeclaration; }
	}

	public final ClassDeclarationContext classDeclaration() throws RecognitionException {
		ClassDeclarationContext _localctx = new ClassDeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_classDeclaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(19);
			match(T__0);
			setState(20);
			match(ID);
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__1) {
				{
				setState(21);
				match(T__1);
				setState(22);
				match(ID);
				}
			}

			setState(25);
			match(T__2);
			setState(29);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(26);
				feature();
				}
				}
				setState(31);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(32);
			match(T__3);
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

	public static class FeatureContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public List<FormalParameterContext> formalParameter() {
			return getRuleContexts(FormalParameterContext.class);
		}
		public FormalParameterContext formalParameter(int i) {
			return getRuleContext(FormalParameterContext.class,i);
		}
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_feature);
		int _la;
		try {
			setState(58);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(34);
				match(ID);
				setState(35);
				match(T__4);
				setState(36);
				type();
				setState(37);
				match(T__5);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(39);
				match(ID);
				setState(40);
				match(T__6);
				setState(49);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ID) {
					{
					setState(41);
					formalParameter();
					setState(46);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__7) {
						{
						{
						setState(42);
						match(T__7);
						setState(43);
						formalParameter();
						}
						}
						setState(48);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
				}

				setState(51);
				match(T__8);
				setState(52);
				match(T__4);
				setState(53);
				type();
				setState(54);
				match(T__2);
				setState(55);
				expression(0);
				setState(56);
				match(T__3);
				}
				break;
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

	public static class FormalParameterContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public FormalParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formalParameter; }
	}

	public final FormalParameterContext formalParameter() throws RecognitionException {
		FormalParameterContext _localctx = new FormalParameterContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_formalParameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(ID);
			setState(61);
			match(T__4);
			setState(62);
			type();
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

	public static class TypeContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TypeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_type; }
	}

	public final TypeContext type() throws RecognitionException {
		TypeContext _localctx = new TypeContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_type);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			_la = _input.LA(1);
			if ( !(_la==T__9 || _la==ID) ) {
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

	public static class ExpressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TypeContext type() {
			return getRuleContext(TypeContext.class,0);
		}
		public TerminalNode INT() { return getToken(YAPLParser.INT, 0); }
		public TerminalNode STRING() { return getToken(YAPLParser.STRING, 0); }
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		return expression(0);
	}

	private ExpressionContext expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressionContext _localctx = new ExpressionContext(_ctx, _parentState);
		ExpressionContext _prevctx = _localctx;
		int _startState = 10;
		enterRecursionRule(_localctx, 10, RULE_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				{
				setState(67);
				match(T__10);
				setState(68);
				expression(0);
				setState(69);
				match(T__11);
				setState(70);
				expression(0);
				setState(71);
				match(T__12);
				setState(72);
				expression(0);
				setState(73);
				match(T__13);
				}
				break;
			case 2:
				{
				setState(75);
				match(T__14);
				setState(76);
				expression(0);
				setState(77);
				match(T__15);
				setState(78);
				expression(0);
				setState(79);
				match(T__16);
				}
				break;
			case 3:
				{
				setState(81);
				match(T__2);
				setState(82);
				expression(0);
				setState(87);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__5) {
					{
					{
					setState(83);
					match(T__5);
					setState(84);
					expression(0);
					}
					}
					setState(89);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(90);
				match(T__3);
				}
				break;
			case 4:
				{
				setState(92);
				match(T__17);
				setState(93);
				match(ID);
				setState(94);
				match(T__4);
				setState(95);
				type();
				setState(98);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
				case 1:
					{
					setState(96);
					match(T__18);
					setState(97);
					expression(0);
					}
					break;
				}
				setState(102);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
				case 1:
					{
					setState(100);
					match(T__19);
					setState(101);
					expression(0);
					}
					break;
				}
				}
				break;
			case 5:
				{
				setState(104);
				match(T__20);
				setState(105);
				type();
				}
				break;
			case 6:
				{
				setState(106);
				match(T__21);
				setState(107);
				expression(18);
				}
				break;
			case 7:
				{
				setState(108);
				match(ID);
				setState(109);
				match(T__18);
				setState(110);
				expression(17);
				}
				break;
			case 8:
				{
				setState(111);
				match(T__31);
				setState(112);
				expression(7);
				}
				break;
			case 9:
				{
				setState(113);
				match(T__6);
				setState(114);
				expression(0);
				setState(115);
				match(T__8);
				}
				break;
			case 10:
				{
				setState(117);
				match(ID);
				}
				break;
			case 11:
				{
				setState(118);
				match(INT);
				}
				break;
			case 12:
				{
				setState(119);
				match(STRING);
				}
				break;
			case 13:
				{
				setState(120);
				match(T__32);
				}
				break;
			case 14:
				{
				setState(121);
				match(T__33);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(180);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(178);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,14,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(124);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(125);
						match(T__24);
						setState(126);
						expression(15);
						}
						break;
					case 2:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(127);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(128);
						match(T__25);
						setState(129);
						expression(14);
						}
						break;
					case 3:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(130);
						if (!(precpred(_ctx, 12))) throw new FailedPredicateException(this, "precpred(_ctx, 12)");
						setState(131);
						match(T__26);
						setState(132);
						expression(13);
						}
						break;
					case 4:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(133);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(134);
						match(T__27);
						setState(135);
						expression(12);
						}
						break;
					case 5:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(136);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(137);
						match(T__28);
						setState(138);
						expression(11);
						}
						break;
					case 6:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(139);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(140);
						match(T__29);
						setState(141);
						expression(10);
						}
						break;
					case 7:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(142);
						if (!(precpred(_ctx, 8))) throw new FailedPredicateException(this, "precpred(_ctx, 8)");
						setState(143);
						match(T__30);
						setState(144);
						expression(9);
						}
						break;
					case 8:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(145);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(146);
						match(T__22);
						setState(147);
						match(ID);
						setState(148);
						match(T__6);
						setState(157);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__6) | (1L << T__10) | (1L << T__14) | (1L << T__17) | (1L << T__20) | (1L << T__21) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << ID) | (1L << INT) | (1L << STRING))) != 0)) {
							{
							setState(149);
							expression(0);
							setState(154);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__7) {
								{
								{
								setState(150);
								match(T__7);
								setState(151);
								expression(0);
								}
								}
								setState(156);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(159);
						match(T__8);
						}
						break;
					case 9:
						{
						_localctx = new ExpressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expression);
						setState(160);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(161);
						match(T__23);
						setState(162);
						type();
						setState(163);
						match(T__22);
						setState(164);
						match(ID);
						setState(165);
						match(T__6);
						setState(174);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__2) | (1L << T__6) | (1L << T__10) | (1L << T__14) | (1L << T__17) | (1L << T__20) | (1L << T__21) | (1L << T__31) | (1L << T__32) | (1L << T__33) | (1L << ID) | (1L << INT) | (1L << STRING))) != 0)) {
							{
							setState(166);
							expression(0);
							setState(171);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__7) {
								{
								{
								setState(167);
								match(T__7);
								setState(168);
								expression(0);
								}
								}
								setState(173);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
						}

						setState(176);
						match(T__8);
						}
						break;
					}
					} 
				}
				setState(182);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,15,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 5:
			return expression_sempred((ExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expression_sempred(ExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 14);
		case 1:
			return precpred(_ctx, 13);
		case 2:
			return precpred(_ctx, 12);
		case 3:
			return precpred(_ctx, 11);
		case 4:
			return precpred(_ctx, 10);
		case 5:
			return precpred(_ctx, 9);
		case 6:
			return precpred(_ctx, 8);
		case 7:
			return precpred(_ctx, 16);
		case 8:
			return precpred(_ctx, 15);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3(\u00ba\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2\6\2\20\n\2\r\2\16\2\21\3\2"+
		"\3\2\3\3\3\3\3\3\3\3\5\3\32\n\3\3\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\3"+
		"\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4"+
		"\5\4\64\n\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4=\n\4\3\5\3\5\3\5\3\5\3\6\3"+
		"\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\7\7X\n\7\f\7\16\7[\13\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7e"+
		"\n\7\3\7\3\7\5\7i\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\5\7}\n\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3"+
		"\7\3\7\7\7\u009b\n\7\f\7\16\7\u009e\13\7\5\7\u00a0\n\7\3\7\3\7\3\7\3\7"+
		"\3\7\3\7\3\7\3\7\3\7\3\7\7\7\u00ac\n\7\f\7\16\7\u00af\13\7\5\7\u00b1\n"+
		"\7\3\7\3\7\7\7\u00b5\n\7\f\7\16\7\u00b8\13\7\3\7\2\3\f\b\2\4\6\b\n\f\2"+
		"\3\4\2\f\f%%\2\u00d6\2\17\3\2\2\2\4\25\3\2\2\2\6<\3\2\2\2\b>\3\2\2\2\n"+
		"B\3\2\2\2\f|\3\2\2\2\16\20\5\4\3\2\17\16\3\2\2\2\20\21\3\2\2\2\21\17\3"+
		"\2\2\2\21\22\3\2\2\2\22\23\3\2\2\2\23\24\7\2\2\3\24\3\3\2\2\2\25\26\7"+
		"\3\2\2\26\31\7%\2\2\27\30\7\4\2\2\30\32\7%\2\2\31\27\3\2\2\2\31\32\3\2"+
		"\2\2\32\33\3\2\2\2\33\37\7\5\2\2\34\36\5\6\4\2\35\34\3\2\2\2\36!\3\2\2"+
		"\2\37\35\3\2\2\2\37 \3\2\2\2 \"\3\2\2\2!\37\3\2\2\2\"#\7\6\2\2#\5\3\2"+
		"\2\2$%\7%\2\2%&\7\7\2\2&\'\5\n\6\2\'(\7\b\2\2(=\3\2\2\2)*\7%\2\2*\63\7"+
		"\t\2\2+\60\5\b\5\2,-\7\n\2\2-/\5\b\5\2.,\3\2\2\2/\62\3\2\2\2\60.\3\2\2"+
		"\2\60\61\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\63+\3\2\2\2\63\64\3\2\2\2"+
		"\64\65\3\2\2\2\65\66\7\13\2\2\66\67\7\7\2\2\678\5\n\6\289\7\5\2\29:\5"+
		"\f\7\2:;\7\6\2\2;=\3\2\2\2<$\3\2\2\2<)\3\2\2\2=\7\3\2\2\2>?\7%\2\2?@\7"+
		"\7\2\2@A\5\n\6\2A\t\3\2\2\2BC\t\2\2\2C\13\3\2\2\2DE\b\7\1\2EF\7\r\2\2"+
		"FG\5\f\7\2GH\7\16\2\2HI\5\f\7\2IJ\7\17\2\2JK\5\f\7\2KL\7\20\2\2L}\3\2"+
		"\2\2MN\7\21\2\2NO\5\f\7\2OP\7\22\2\2PQ\5\f\7\2QR\7\23\2\2R}\3\2\2\2ST"+
		"\7\5\2\2TY\5\f\7\2UV\7\b\2\2VX\5\f\7\2WU\3\2\2\2X[\3\2\2\2YW\3\2\2\2Y"+
		"Z\3\2\2\2Z\\\3\2\2\2[Y\3\2\2\2\\]\7\6\2\2]}\3\2\2\2^_\7\24\2\2_`\7%\2"+
		"\2`a\7\7\2\2ad\5\n\6\2bc\7\25\2\2ce\5\f\7\2db\3\2\2\2de\3\2\2\2eh\3\2"+
		"\2\2fg\7\26\2\2gi\5\f\7\2hf\3\2\2\2hi\3\2\2\2i}\3\2\2\2jk\7\27\2\2k}\5"+
		"\n\6\2lm\7\30\2\2m}\5\f\7\24no\7%\2\2op\7\25\2\2p}\5\f\7\23qr\7\"\2\2"+
		"r}\5\f\7\tst\7\t\2\2tu\5\f\7\2uv\7\13\2\2v}\3\2\2\2w}\7%\2\2x}\7&\2\2"+
		"y}\7\'\2\2z}\7#\2\2{}\7$\2\2|D\3\2\2\2|M\3\2\2\2|S\3\2\2\2|^\3\2\2\2|"+
		"j\3\2\2\2|l\3\2\2\2|n\3\2\2\2|q\3\2\2\2|s\3\2\2\2|w\3\2\2\2|x\3\2\2\2"+
		"|y\3\2\2\2|z\3\2\2\2|{\3\2\2\2}\u00b6\3\2\2\2~\177\f\20\2\2\177\u0080"+
		"\7\33\2\2\u0080\u00b5\5\f\7\21\u0081\u0082\f\17\2\2\u0082\u0083\7\34\2"+
		"\2\u0083\u00b5\5\f\7\20\u0084\u0085\f\16\2\2\u0085\u0086\7\35\2\2\u0086"+
		"\u00b5\5\f\7\17\u0087\u0088\f\r\2\2\u0088\u0089\7\36\2\2\u0089\u00b5\5"+
		"\f\7\16\u008a\u008b\f\f\2\2\u008b\u008c\7\37\2\2\u008c\u00b5\5\f\7\r\u008d"+
		"\u008e\f\13\2\2\u008e\u008f\7 \2\2\u008f\u00b5\5\f\7\f\u0090\u0091\f\n"+
		"\2\2\u0091\u0092\7!\2\2\u0092\u00b5\5\f\7\13\u0093\u0094\f\22\2\2\u0094"+
		"\u0095\7\31\2\2\u0095\u0096\7%\2\2\u0096\u009f\7\t\2\2\u0097\u009c\5\f"+
		"\7\2\u0098\u0099\7\n\2\2\u0099\u009b\5\f\7\2\u009a\u0098\3\2\2\2\u009b"+
		"\u009e\3\2\2\2\u009c\u009a\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u00a0\3\2"+
		"\2\2\u009e\u009c\3\2\2\2\u009f\u0097\3\2\2\2\u009f\u00a0\3\2\2\2\u00a0"+
		"\u00a1\3\2\2\2\u00a1\u00b5\7\13\2\2\u00a2\u00a3\f\21\2\2\u00a3\u00a4\7"+
		"\32\2\2\u00a4\u00a5\5\n\6\2\u00a5\u00a6\7\31\2\2\u00a6\u00a7\7%\2\2\u00a7"+
		"\u00b0\7\t\2\2\u00a8\u00ad\5\f\7\2\u00a9\u00aa\7\n\2\2\u00aa\u00ac\5\f"+
		"\7\2\u00ab\u00a9\3\2\2\2\u00ac\u00af\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad"+
		"\u00ae\3\2\2\2\u00ae\u00b1\3\2\2\2\u00af\u00ad\3\2\2\2\u00b0\u00a8\3\2"+
		"\2\2\u00b0\u00b1\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b3\7\13\2\2\u00b3"+
		"\u00b5\3\2\2\2\u00b4~\3\2\2\2\u00b4\u0081\3\2\2\2\u00b4\u0084\3\2\2\2"+
		"\u00b4\u0087\3\2\2\2\u00b4\u008a\3\2\2\2\u00b4\u008d\3\2\2\2\u00b4\u0090"+
		"\3\2\2\2\u00b4\u0093\3\2\2\2\u00b4\u00a2\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6"+
		"\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\r\3\2\2\2\u00b8\u00b6\3\2\2\2"+
		"\22\21\31\37\60\63<Ydh|\u009c\u009f\u00ad\u00b0\u00b4\u00b6";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}